# Threat Intelligence (TI) Rotation

> Research draft for the ORTSOC Initial Orientation Website. Pending review by the Threat Intelligence Rotation Lead.
> This page is a high-level overview. Never put client names, scan results, or other TLP:AMBER material on this site.

## What TI Does

Cyber Threat Intelligence is the **systematic collection, analysis, and sharing of information about threats** to an organization, so decision-makers at every level know what is happening and what is coming (adapted from FIRST CTI SIG).

Four ideas to keep in mind:

- **Systematic:** TI follows a process and a routine. It is a habit, not random browsing.
- **Specific and actionable:** "Windows is under attack" is not intelligence. The client needs to know which version, which patch, and what to do about it.
- **Audience-aware:** who you are writing for changes what you write (see the four levels below).
- **Situational awareness:** the goal is to help clients predict and prepare, not just react.

There is far more threat information out there than anyone can report. Your job is to find what matters **to the client** and turn it into something they can act on.

### Four Levels of Intelligence

| Level | Focus | Typical audience |
|---|---|---|
| **Strategic** | Threats that affect business decisions | Leadership |
| **Operational** | Threats specific to an organization, such as an observed behavior or an expected attack | Defenders, sysadmins |
| **Tactical** | Tactics, Techniques, and Procedures (TTPs) | Security teams |
| **Technical** | IOCs, IOAs, forensic evidence | Analysts, tools |

As a TI student, you will mostly **consume** tactical and technical intelligence and **create** strategic and operational intelligence.

**What you will be evaluated on:**

- Assessing the quality and reliability of threat intelligence sources
- Writing actionable intelligence for clients
- Alerting on high severity events
- Interpreting vulnerability scan results and reporting them to clients
- Mapping threat actors to TTPs with MITRE ATT&CK
- Giving Network Security Monitoring the information it needs to monitor and investigate

## What You Will Produce

| Output | Audience | Focus | How often |
|---|---|---|---|
| **Daily threat news** | You and your team | Staying current | Every shift |
| **Threat Newsletter** | IT professionals at ORTSOC Consortium members | Strategic | Once per rotation, as a group |
| **Urgent Threat Notification** | Client system administrators | Operational | When NSM finds a high severity event affecting multiple clients |
| **Vulnerability Report** | The client | Simple, actionable fixes | Weekly |
| **Risk Profile** | A specific client | Industry risks, current and emerging threats, prioritized recommendations | Once per rotation, in a small group |

The Risk Profile pulls everything together. You research the client's industry, review the software and hardware they use, estimate business impact, prioritize threats, work with NSM and Security Engineering to find monitoring gaps, and recommend client actions.

## Week 1 Checklist

1. Read about IOCs (CrowdStrike and Splunk articles linked in Canvas).
2. Read CISA's **Best Practices for MITRE ATT&CK Mapping**.
3. Complete the **Mapping MITRE ATT&CK** practice exercise. Try it before looking at the solution.
4. Define the terms in the **TI Glossary** in your own words (see below).
5. Take the **TI Orientation Knowledge Check**.
6. Watch Slack for your group's first vulnerability scan.

## Key Concepts

### IOCs vs. IOAs

| | Indicator of Compromise (IOC) | Indicator of Attack (IOA) |
|---|---|---|
| **What it is** | Forensic evidence that a breach **already happened** | Behavior showing an attack **in progress** |
| **Focus** | Artifacts the attacker left behind | The attacker's actions and intent |
| **Timing** | Reactive, after the fact | Proactive, during the attack |
| **Examples** | A malicious file hash, a known C2 IP or domain | Code execution, privilege escalation in progress |

**Three common IOC types:**

- **Network-based:** malicious IPs, domains, unusual traffic
- **File-based:** file hashes, file names, file paths
- **Behavioral:** repeated failed logins, unusual spikes in traffic or database reads

**Common warning signs:** unusual outbound traffic, traffic to or from countries the client has no business with, spikes in failed logins, odd admin account activity, unusual DNS requests, unexpected registry changes, and large compressed files in strange places.

**Pyramid of Pain (David Bianco):** some indicators are easy for attackers to change (hashes, IPs) and some are hard (their TTPs). Detecting and blocking behaviors hurts attackers far more than blocking a single IP. That is why TI focuses on TTPs, not just IOC lists.

IOCs go stale. Validate them, add context (source, date, related artifacts), and retire old ones so they don't cause false positives.

## MITRE ATT&CK Basics

[MITRE ATT&CK](https://attack.mitre.org/) is a free knowledge base of real-world adversary behavior. It has four levels:

| Level | Answers | Example |
|---|---|---|
| **Tactic** | **Why**: the attacker's goal | Credential Access [TA0006] |
| **Technique** | **How** they reach the goal | OS Credential Dumping [T1003] |
| **Sub-technique** | A more specific how | LSASS Memory [T1003.001] |
| **Procedure** | **What** they actually did | The specific tool and commands used |

Attackers don't move through tactics left to right in order, and they don't use every tactic.

### How to Map Behavior to ATT&CK (CISA)

1. **Find the behavior.** Look for *how* the attacker interacted with systems, not just IOCs.
2. **Research the behavior.** Read the original reports and search key verbs on the ATT&CK site, such as "created a scheduled task."
3. **Translate it into a tactic.** Ask *why* they did it: steal data, escalate privileges, stay hidden?
4. **Identify the technique.** Compare the behavior to the techniques under that tactic. One behavior can map to more than one technique.
5. **Identify the sub-technique.** Only stop at the parent technique if there isn't enough detail.
6. **Compare with other analysts.** Mapping is a team sport. Peer review catches what you missed.

**Example:** "HTTP command and control traffic over port 8088" maps to both Web Protocols [T1071.001] and Non-Standard Port [T1571].

### Common Mapping Mistakes

| Mistake | Example | Fix |
|---|---|---|
| **Leaping to conclusions** | Mapping traffic on port 443 to HTTPS without confirming the protocol | Only map what the evidence supports |
| **Missed opportunities** | Mapping VPN access to External Remote Services but missing Valid Accounts | Look for every technique a behavior implies |
| **Miscategorization** | Calling file deletion "Data Destruction" when it was hiding tracks | Read technique descriptions carefully |

In reports, put technique IDs inline in brackets, for example: "The actor delivered malware via phishing emails [T1566.002]."

## Vulnerability Scanning Workflow

ORTSOC uses **OpenVAS (Greenbone)** for vulnerability scanning, and TI works with Security Engineering on it.

| When | What to do |
|---|---|
| **Tuesday to Friday** | Find the scan in the client's folder in Nextcloud Collectives. Sort, research, and prioritize the findings, then write a simple report for the client. |
| **By Monday** | Send the report to the client (within 5 business days). |
| **Tuesday** | Start again with the next scan. |

**How to prioritize:** use the **CVSS** score for severity, look up each **CVE** for details and fixes, and think about real risk to the client (Risk = Threat x Vulnerability). A critical vulnerability on an exposed server matters more than the same one on an isolated machine.

> **Scans are TLP:AMBER.** Only open them on ORTSOC devices. Write reports in Nextcloud. Slack is fine for coordinating, but never post client names together with vulnerability details there.

This is a newer ORTSOC service, so the process may change. Watch Slack for updates.

## Glossary

| Term | Meaning |
|---|---|
| **Threat Actor** | A person or group that carries out or intends cyberattacks |
| **TTPs** | Tactics, Techniques, and Procedures: how a threat actor operates |
| **Attack Surface** | Every point where an attacker could try to get in |
| **APT** | Advanced Persistent Threat: a skilled actor that targets specific organizations over a long time, quietly |
| **IOC** | Indicator of Compromise: evidence a breach happened |
| **IOA** | Indicator of Attack: behavior showing an attack in progress |
| **Threat Intelligence** | Analyzed information about threats that supports decisions |
| **Phishing** | Fake emails or sites that trick people into giving up information or running malware |
| **Vulnerability** | A weakness or flaw that could be exploited |
| **CVE** | A unique ID for a publicly known vulnerability, like CVE-2023-12345 |
| **CVSS** | A 0 to 10 score showing how severe a vulnerability is |
| **Zero-Day** | An attack on a flaw the vendor doesn't know about yet, so no patch exists |
| **Risk** | The potential for loss when a threat exploits a vulnerability |
| **Remediation** | Fixing the problem, such as patching or changing a configuration |
| **False Positive** | An alert that flags harmless activity as malicious |

For official definitions, see the [NIST CSRC Glossary](https://csrc.nist.gov/glossary) and the [SOCRadar CTI Glossary](https://socradar.io/resources/radar/cti-glossary/).

## Beginner Tips

- Read threat news at the start of every shift. A few minutes a day builds the habit the rotation expects.
- Always ask "does this affect our clients?" before reporting anything.
- Check how reliable a source is before you trust it. Vendor blogs, CISA advisories, and random posts are not equal.
- Put ATT&CK technique IDs in your notes as you go. It makes the newsletter and Risk Profile much faster to write.
- If you spot something urgent, loop in NSM right away. TI and NSM work closely together.
- Keep anything from scans off Slack, personal notes, and personal devices.

## Related Pages

- [Network Security Monitoring](nsm.md): TI shares IOCs with NSM, and NSM flags events that may need an Urgent Threat Notification
- [Nextcloud & Playbooks](../tools/nextcloud.md): where scans and reports live

## Sources

- ORTSOC CS 424 Canvas: Introduction to Threat Intelligence; Threat Intelligence Week 1; Threat Intelligence Glossary; Vulnerability Scanning; Mapping MITRE ATT&CK
- FIRST Cyber Threat Intelligence SIG
- CrowdStrike, Indicators of Compromise (IOC) Security Explained
- Splunk, Indicators of Compromise (IoCs): An Introductory Guide
- CISA, Best Practices for MITRE ATT&CK Mapping (January 2023)
- MITRE ATT&CK, attack.mitre.org
- Greenbone OpenVAS documentation
