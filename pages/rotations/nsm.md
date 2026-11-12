---
title: "Network Security Monitoring (NSM) Rotation"
parent: Rotations
---

# Network Security Monitoring (NSM) Rotation

> Research draft for the ORTSOC Initial Orientation Website. Pending review by the NSM Rotation Lead.
> All IP addresses below are generic examples. Never put real client names, IPs, or hostnames in this guide.

## What NSM Does

In the NSM rotation, you monitor, analyze, investigate, and report on security events and incidents across ORTSOC client networks. You apply networking and security concepts to your investigations and follow ORTSOC playbooks while doing it.

**What you will be evaluated on:**

- Monitoring, analyzing, and investigating suspicious logs and alerts
- Categorizing the severity of an event or incident
- Responding with the right actions based on severity
- Communicating professionally with students, mentors, and clients
- Creating, maintaining, and following ORTSOC playbooks, policies, and procedures
- Creating and updating tickets for suspicious events
- Documenting findings and communication about each event

## Tools You Will Use

| Tool | What it's for |
|---|---|
| **Kibana** | Where you spend most of your shift. Search client and ORTSOC logs, view dashboards, and manage alerts. |
| **Zeek logs** | Network metadata in Kibana, such as `zeek.conn` (connections), `zeek.ssl` (TLS sessions), `zeek.dns`, and `zeek.http`. |
| **Suricata alerts** | IDS alerts that fire on known malicious patterns. |
| **RTIR** | Ticketing system. Every suspicious event or alert gets a ticket. |
| **Nextcloud Collectives** | Client repo. Where you claim a client and find client info. |
| **Slack #nsm-handoffs** | Where you post your pass down at the end of every shift. |
| **AbuseIPDB, GreyNoise, VirusTotal** | Free sites for checking whether an IP or domain is known to be malicious. |

## Daily Checklist

1. **Claim a client** in Nextcloud (click "Collectives" in the top toolbar).
2. **Verify all sensors are active.**
3. **Review hand-offs** in #nsm-handoffs.
4. **Review open tickets.** If any are open, work those first.
5. **Review recently resolved tickets** to see what others found.
6. **Manage open alerts** in Kibana.
7. **Hunt.** Look for suspicious activity on your client's network even if no alert fired.
8. **Close out.** Start 15 minutes before you leave so you have time for tickets and hand-off.

## Kibana Basics

**First login:** Log in with your ONID and the initial password from the Canvas Kibana walkthrough. Change your password right away.

**Core skills to learn first:**

- Finding client and ORTSOC logs (switch the data view in Discover)
- Changing the time range (top right time picker)
- Adding filters (hover a field value and click the magnifying glass with **+**)
- Writing queries in the search bar (KQL)
- Opening dashboards
- Finding rules and alerts

### KQL Cheat Sheet

KQL is the default query language in Kibana. It only filters data. It does not sort or count.

| What you want | Example |
|---|---|
| Field equals a value | `source.ip: "10.0.0.5"` |
| Combine conditions | `source.ip: "10.0.0.5" and event.dataset: "zeek.conn"` |
| Either condition | `source.ip: "10.0.0.5" or destination.ip: "10.0.0.5"` |
| Exclude something | `event.dataset: "zeek.conn" and not destination.port: 443` |
| Multiple values for one field | `destination.port: (22 or 3389 or 445)` |
| Range | `destination.port >= 1024` |
| Field exists | `ssl.server_name: *` |
| Wildcard | `dns.query.name: *.example.com` |

**Tips:**

- Put IPs and multi-word values in quotes.
- `and` runs before `or`. Use parentheses to group: `event.dataset: "zeek.conn" and (source.ip: "10.0.0.5" or destination.ip: "10.0.0.5")`
- If a field name returns nothing, type part of it (like `bytes` or `packets`) into the field search box on the left sidebar to find the exact name your logs use.
- Add useful fields as columns by hovering the field and clicking **+**.

## Example Investigation Workflow

This is a typical flow for checking whether an external IP is talking to a client host. Example IPs: client host `10.0.0.5`, external IP `203.0.113.50`.

**1. Find the activity.**
```
source.ip: "203.0.113.50" and destination.ip: "10.0.0.5"
```
Set the time range wide (like Last 7 days). Note the hit count and the first and last timestamps.

**2. See which log sources have it.** Remove `event.dataset` from the query, then click `event.dataset` in the sidebar to see every source that logged this traffic (Zeek, Suricata, firewall, endpoint).

**3. Check if traffic went both ways.**
- In `zeek.conn`, look at `zeek.connection.state`. `SF` means a normal connection that was opened and closed by both sides. `S0` or `REJ` means the other side never answered or refused.
- Look at the bytes fields for each direction (search the sidebar for `bytes`).
- In `zeek.ssl`, `ssl.established: true` means the TLS handshake finished, so both sides talked.

**4. Pivot between Zeek logs.** Every Zeek log for the same connection shares an ID. Copy `zeek.session_id` from an SSL log and search:
```
event.dataset: "zeek.conn" and zeek.session_id: "PASTE_ID_HERE"
```
This shows the connection details for that exact session.

**5. Figure out who started it.** The side with a port that keeps changing between connections is the client side, so it's the one initiating. The side with the fixed port is the server.

**6. Read the volume.**
- Small bytes both ways, repeated at regular intervals: possible beaconing or check-ins
- Large bytes from the internal host outward: possible data exfiltration
- Large bytes from the external host inward: possible download or payload

**7. Research the IP.** Check AbuseIPDB (score, report categories), GreyNoise (is it a mass internet scanner or targeted?), and VirusTotal. Don't ping, scan, or visit the IP yourself.

**8. Decide and document.** Write up findings in RTIR and categorize the event (see below). Escalate to a mentor or Rotation Lead if it looks targeted or successful.

> `event.duration` in Kibana is in nanoseconds. Divide by 1,000,000,000 to get seconds.

## Categorizing Events

| Term | Meaning | Example |
|---|---|---|
| **Event** | Any observable occurrence in a system or network (NIST SP 800-61) | A file moved, a user clicking an icon |
| **Security Event** | Something that may indicate a policy violation or failed control (ISO 27001) | A failed SSH attempt, a sudo attempt by a non-sudoer |
| **Security Incident** | A violation or imminent threat of violating security policies (NIST SP 800-61) | A login portal being brute forced, ransomware deployed |
| **Data Breach** | Loss of control or unauthorized access to sensitive information (NIST SP 800-53A) | An attacker downloads proprietary data |

**Severity** (based on the CISA National Cyber Incident Scoring System):

| Low | Medium | High | Critical |
|---|---|---|---|
| Unlikely to affect operations | May affect operations | Likely to cause demonstrable impact | Likely to cause significant impact |

Common closing statuses: **false positive** (alert fired but nothing bad happened) and **benign positive** (the activity was real but not harmful).

## Writing Tickets in RTIR

Every suspicious event and alert needs a ticket. Log in with `ONID@ortsoc.oregonstate.edu` and your FreeIPA password.

**1. Set the Basics first (top right):**
- **Queue:** the client the ticket is about
- **Status:** starts as "new." Change it to "open" if you leave your shift before it's resolved.
- **Priority:** use the priority guidelines on Canvas

**2. Subject format:** `[Kibana Rule Name]-[MM.DD.YY]`
Example: `Attempted Information Leak-09.03.26`

**3. Body:** be as detailed as possible. Use who, what, when, how:
- **When:** dates and times of every related event
- **Who:** IPs, URLs, MAC addresses, any entity involved
- **How:** ports, protocols, communication direction
- **What:** your research on those entities (AbuseIPDB, port lookups, malware research)

**4. Attach evidence:** PCAPs, screenshots, research notes. Then click **Create**.

**Updating a ticket:** open it, scroll to the bottom, click **Reply** or **Comment**, add your update, and click **Update Ticket**.

**What a good ticket has:** concise descriptions, a timeline of events, analysis in every update, severity or category changes noted, and links to every site or article you used.

## Shift Hand-off

Post in **#nsm-handoffs** before you leave:

- **Open tickets:** ticket number, how far you got, next steps
- **Closed tickets:** what you found and the status (false positive, benign positive, etc.)
- **Anything notable:** for example, "300k+ alerts related to scanning from one external network"

## Incident Response Reports

For any substantial incident that has been resolved, the NSM rotation writes an after-incident report using the template on Canvas. A member of the rotation presents it to the ORTSOC class on Friday.

- Write reports together with others in the rotation. If you worked the incident, help write it.
- No report is needed while an incident is still ongoing or unresolved by the client.
- The most important section is **Post-Incident Activity**: what the SOC could do better next time. This is never about blame, and naming and shaming is not allowed.
- Not sure if something needs a report? Ask a mentor.

## Beginner Tips

- Open tickets come before new alerts. Always.
- Start your close out 15 minutes early. Tickets and hand-offs take longer than you think.
- When a field doesn't exist, search the sidebar for part of its name before giving up.
- A scary AbuseIPDB score doesn't automatically mean compromise. Check who started the connection and how much data moved.
- Check GreyNoise for any noisy external IP. If it's a mass scanner hitting everyone, it's usually not targeted.
- Write tickets as you go, not at the end of your shift.

## Sources

- ORTSOC CS 424 Canvas: NSM Orientation 1 (Overview), 2 (Kibana Walkthrough), 4 (RTIR Walkthrough), 6 (Incident Response Reports)
- ORTSOC Tickets guide, Jordan Hankin, Spring 2025
- Elastic, Kibana Query Language (KQL) overview
- Dattell, How to Query Elasticsearch in Kibana
- NIST SP 800-61r2, NIST SP 800-53Ar5, ISO 27001, CISA National Cyber Incident Scoring System
- Author's own NSM shift experience (examples generalized)
