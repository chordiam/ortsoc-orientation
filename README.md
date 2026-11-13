# ORTSOC Initial Orientation Website

An internal orientation guide for new ORTSOC students, covering ORTSOC's mission, client services, rotations, core tools, shift expectations, and student tips.

CS 428 Cyber Capstone, Fall 2026. Team: Kaelee Duong (PM), Manasi Chordia, Niki Pandya, Justin Primc. Sponsor: Dave Nevin.

## Folder Layout

```
index.html                  The website (no setup needed)
assets/nav.js               Sidebar menu: add new pages here
assets/marked.min.js        Turns Markdown into the web page
pages/
  home.md                   Home page
  mission.md                ORTSOC mission, structure, policies
  client-services.md        Types of clients and services ORTSOC provides
  shift-expectations.md     What a typical shift looks like
  tips.md                   Tips from current and past students
  rotations/                One page per rotation (nsm.md, ...)
  tools/                    One walkthrough per tool (kibana.md, ...)
```

## Page Status

| Page | Owner | Status |
|---|---|---|
| rotations/nsm.md | Manasi | Draft, Rotation Lead review pending |
| rotations/pentest.md | Justin | Draft, Rotation Lead review pending |
| tools/kibana.md | Manasi | Draft |
| tools/rtir.md | Manasi | Draft |
| tools/nextcloud.md | Manasi | Draft |
| mission.md | Justin | Draft |
| client-services.md | Justin | Draft |
| shift-expectations.md | Justin | Draft |
| tips.md | | |

Update this table when you start or finish a page.

## Rotation Coverage Plan

Each rotation is researched by a teammate who is in that rotation or can observe it during their shift. If someone's rotation or shift changes, reassign the row here so no rotation gets dropped.

| Rotation | Researched by | Backup | Status |
|---|---|---|---|
| Network Security Monitoring (NSM) | Manasi | | Draft done |
| Penetration Testing | Justin | | Draft done |
| | | | |
| | | | |
| | | | |

## Adding a New Page

1. Create the Markdown file, for example `pages/rotations/threat_intel.md`.
2. Add one line to `assets/nav.js` so it shows in the sidebar:
   ```js
   { title: "Threat Intelligence", path: "pages/rotations/threat_intel.md" },
   ```

## Preview the Site

From the repo folder, run:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000. Press `Ctrl+C` to stop.

## How to Add Content

1. Get the latest version:
   ```bash
   git pull
   ```
2. Edit or create your page in Markdown.
3. Save and push:
   ```bash
   git add .
   git commit -m "Short description of what you changed"
   git push
   ```
4. Post in the team chat when a page is ready for review.

## Rules

- **No client data.** Never include real client names, IPs, hostnames, or incident details. Use generic examples like `10.0.0.5` and `203.0.113.50`.
- **No passwords or secrets**, including default ones.
- **List your sources** at the bottom of each page.
- **Keep it beginner level.** Link to Canvas modules for anything in-depth.
