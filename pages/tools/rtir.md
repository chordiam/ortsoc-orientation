---
title: "RTIR"
parent: Tools
nav_order: 2
---

# RTIR: Beginner Ticketing Walkthrough

> Draft for the ORTSOC Initial Orientation Website (Task 2.2.4, Tool Section).
> Builds on the RTIR Walkthrough and ORTSOC Tickets guide on Canvas. All IPs are generic examples. Never add real client names, IPs, or hostnames.

## What RTIR Is

RTIR (Request Tracker for Incident Response) is ORTSOC's ticketing system. **Every suspicious event and alert gets a ticket.** Tickets are how the next shift, your mentors, and the client know what you found, so a ticket should make sense to someone who never saw the alert.

URL: `https://ticketing.ortsoc.oregonstate.edu`

## 1. Log In

- **Username:** `ONID@ortsoc.oregonstate.edu`
- **Password:** your FreeIPA password

## 2. Check Existing Tickets First

Before you make a new ticket, search for the alert or IP in the **Search Ticket** bar. If a ticket already exists, add to it instead of creating a duplicate (see step 6).

## 3. Create a Ticket

Click **Create new ticket** (top right, next to the search bar), or hover over **Home** and choose it from the dropdown.

## 4. Set the Basics First

In the **Basics** box (top right), set these before writing anything else:

| Field | What to put |
|---|---|
| **Queue** | The ORTSOC client this ticket is about |
| **Status** | Starts as **new**. Change to **open** if you leave your shift before it is resolved. |
| **Priority** | Use the priority guidelines on Canvas |

## 5. Fill In Requestors, Subject, and Body

**Requestors:** autofills with your name. If you are working the ticket with someone, add them too.

**Subject:** this is the first thing anyone sees when searching, so always use this format:

```
[Kibana Rule Name]-[MM.DD.YY]
```

Example: an alert named "Attempted Information Leak" that you started investigating on September 3, 2026:

```
Attempted Information Leak-09.03.26
```

**Body:** be as detailed as possible. Think like an investigator and answer who, what, when, and how:

| Question | Include |
|---|---|
| **When** | Dates and times of every related event (first seen, last seen) |
| **Who** | IPs, URLs, MAC addresses, hostnames, any entity involved |
| **How** | Ports, protocols, and which direction the traffic went |
| **What** | Your research: AbuseIPDB, GreyNoise, port lookups, malware research |

**Attachments:** drag in PCAPs, screenshots, and research notes. Then click **Create**.

### Example Ticket Body

> **Findings:** External IP 203.0.113.50 connected to client host 10.0.0.5 repeatedly between 10/04 06:00 and 10/06 08:37 (61 completed connections).
>
> - **Direction:** inbound. The external IP's port changed every connection, so it started them.
> - **Connections:** Zeek conn state SF, TLS handshakes completed, mostly under 10 KB each way. Largest: about 4 KB out, 57 bytes back.
> - **Research:** AbuseIPDB 94% (mostly Bad Web Bot and Web App Attack reports). GreyNoise tags it as a web and TLS/SSL crawler seen across 10 countries.
>
> **Conclusion:** Benign positive. Untargeted crawler activity, no sign of data leaving the network. Recommend blocking the IP at the firewall.

## 6. Update a Ticket

You will often work tickets someone else started.

1. Open the ticket to see its timeline of actions and notes.
2. Scroll to the bottom and click **Reply** or **Comment**.
3. Add what you found or changed.
4. Click **Update Ticket**.

## What a Good Ticket Has

- Short, clear descriptions
- A timeline of events
- Analysis in **every** update, not just "looked at this"
- A note whenever the severity or event category changes
- Links to every website or article you used

## Choosing a Category and Severity

See [Categorizing Events](../rotations/nsm.md#categorizing-events) on the NSM page for the difference between an event, security event, security incident, and data breach, plus the Low to Critical severity scale.

Common closing outcomes:

- **False positive:** the alert fired, but nothing actually happened
- **Benign positive:** the activity was real, but not harmful

## Common Beginner Mistakes

| Mistake | Fix |
|---|---|
| Subject doesn't follow the format | Always `[Kibana Rule Name]-[MM.DD.YY]` so it can be searched |
| Duplicate ticket for the same alert | Search first and add to the existing ticket |
| Leaving status as "new" at the end of your shift | Change it to "open" if it's not resolved |
| "Checked IP, looks fine" | Say what you checked, what you found, and why it matters |
| Writing the ticket at the end of your shift | Write as you go, then post it in `#nsm-handoffs` |

## Sources

- ORTSOC CS 424 Canvas: NSM Orientation 4, RTIR Walkthrough
- ORTSOC Tickets guide, Jordan Hankin, Spring 2025
- Author's own NSM shift experience (example generalized)
