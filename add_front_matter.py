"""Add Just the Docs front matter to every page that doesn't have it yet.
Run from the repo root: python3 add_front_matter.py"""
import json, pathlib, re
top = {"mission": ("Mission", 2), "client-services": ("Client Services", 3),
       "shift-expectations": ("Shift Expectations", 4), "tips": ("Tips from Students", 7)}
tools_order = {"kibana": 1, "rtir": 2, "nextcloud": 3}
def title_of(text, stem):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    t = m.group(1).strip() if m else stem.replace("-", " ").title()
    return t.split(":")[0].strip()
changed = []
for p in sorted(pathlib.Path("pages").rglob("*.md")):
    if p.name == "index.md":
        continue
    text = p.read_text(encoding="utf-8")
    if text.lstrip().startswith("---"):
        continue
    stem, parent = p.stem, p.parent.name
    if parent == "pages":
        title, order = top.get(stem, (title_of(text, stem), 8))
        fm = f"---\ntitle: {json.dumps(title)}\nnav_order: {order}\n---\n\n"
    else:
        title = title_of(text, stem)
        fm = f"---\ntitle: {json.dumps(title)}\nparent: {'Rotations' if parent == 'rotations' else 'Tools'}\n"
        if parent == "tools" and stem in tools_order:
            fm += f"nav_order: {tools_order[stem]}\n"
        fm += "---\n\n"
    if not text.strip():
        text = f"# {title}\n\n*This page is coming soon.*\n"
    p.write_text(fm + text, encoding="utf-8")
    changed.append(str(p))
print("Added front matter to:" if changed else "Nothing to change.")
for c in changed:
    print("  " + c)
