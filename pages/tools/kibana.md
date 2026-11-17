---
title: "Kibana"
parent: Tools
nav_order: 1
---

# Kibana: Beginner Walkthrough

> Draft for the ORTSOC Initial Orientation Website (Task 2.2.4, Tool Section).
> Builds on the NSM Orientation 2 Kibana walkthrough on Canvas. All IPs are generic examples. Never add real client names, IPs, or hostnames.

## What Kibana Is

Kibana is the web interface for searching the logs ORTSOC collects from client networks. Most NSM shifts are spent here: reading alerts, searching logs, and gathering evidence for tickets. See the [NSM rotation page](../rotations/nsm.md) for how Kibana fits into a shift.

## 1. Log In and Change Your Password

1. Log in with your ONID and ORTSOC accounts password.

## 2. Find the Right Logs

1. Open the menu (top left) > **Discover**.
2. Click the **data view** dropdown (top left of Discover) and pick the one for the client you claimed.
3. Each row is one log entry. Click the expand arrow on a row to see every field in it.

## 3. Set the Time Range

Use the time picker in the top right. The default is often only the last 15 minutes, so if you see "No results," widen it first.

- **Investigating an alert:** start with a window around the alert time, then widen to Last 7 days to see if it's repeated.
- **Hunting:** Last 24 hours is a good start.

## 4. Search With KQL

Type queries in the search bar at the top and press Enter.

```
source.ip: "10.0.0.5" and event.dataset: "zeek.conn"
```

Most useful datasets for beginners:

| Dataset | Shows |
|---|---|
| `zeek.conn` | Every network connection: who, where, how long, how many bytes |
| `zeek.dns` | Domain lookups |
| `zeek.ssl` | Encrypted (TLS) sessions and server names |
| `zeek.http` | Web requests and URLs |
| `suricata.alert` | IDS alerts on known bad patterns |

Full KQL cheat sheet: see the [NSM rotation page](../rotations/nsm.md#kql-cheat-sheet).

## 5. Add Filters and Columns

- **Filter on a value:** in an expanded row, hover a field value and click the magnifying glass with **+** to include it or **-** to exclude it.
- **Add a column:** hover a field name in the left sidebar and click **+**. Good starting columns: `source.ip`, `destination.ip`, `destination.port`, `event.dataset`.
- **Find a field:** type part of its name (like `bytes` or `session`) in the sidebar search box. Field names can differ between data views.
- **Quick stats:** click a field name in the sidebar to see its top values and percentages.

## 6. Dashboards

Menu > **Dashboards**. Dashboards give a visual overview (top talkers, alert counts, protocols) and are a good place to start hunting. Click any chart segment to filter on it, then open the same filter in Discover for details.

## 7. Alerts and Rules

- **Alerts:** Menu > **Security** > **Alerts**. Shows triggered detections. Click an alert to see the rule name, severity, and the source and destination involved.
- **Rules:** Menu > **Security** > **Rules**. Shows what each detection looks for, which helps you judge whether an alert is a false positive.
- The rule name is what goes in your RTIR ticket subject: `[Kibana Rule Name]-[MM.DD.YY]`.

## 8. Save Your Work

- **Save a search:** top toolbar > **Save** in Discover, so you or the next shift can reopen it.
- **Share:** **Share** > copy link, then paste it in your ticket or hand-off.
- **Screenshots:** take them of key results to attach to RTIR tickets.

## Common Beginner Mistakes

| Problem | Fix |
|---|---|
| "No results" | Widen the time range, then check the data view |
| A field "doesn't exist" | Search the sidebar for part of the name; it may be called something else |
| Query returns nothing | Put IPs and multi-word values in quotes |
| `event.duration` looks huge | It's in nanoseconds. Divide by 1,000,000,000 for seconds |
| Times don't match your notes | Check whether you're reading local time or UTC |

## Sources

- ORTSOC CS 424 Canvas: NSM Orientation 2, Kibana Walkthrough
- Elastic, Kibana Query Language (KQL) overview
- Dattell, How to Query Elasticsearch in Kibana
- Author's own NSM shift experience (examples generalized)
