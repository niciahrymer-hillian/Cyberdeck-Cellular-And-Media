# Cyberdeck-Cellular-And-Media

### Add cellular calling, SMS texting, and music playback to the cyberdeck (LTE HAT + audio) — effectively a DIY phone.

![Chain K](https://img.shields.io/badge/Chain%20K-64748B?style=for-the-badge) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE-GPL) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue?style=for-the-badge)](LICENSE-AGPL)

[🎮 Interactive Tour](docs/interactive/index.html) · [📋 Cheat Sheet](docs/CHEATSHEET.pdf) · [📖 Full Lesson](docs/LESSON.pdf) · [🔗 Resources](docs/RESOURCES.pdf)

<!-- SCREENSHOT PLACEHOLDER: docs/screenshots/overview.png -->

Part of **Chain K — Hardware & Systems Foundations**. Extends **Cyberdeck-Build** — do that project
first, since this one reuses its power-budgeting skill directly.

## What this is

We're adding cellular connectivity and real audio to the cyberdeck, turning it from a portable computer
into something that works without wifi at all. The interesting part isn't the wiring — it's the modem:
an LTE HAT talks to Linux over a serial port using **AT commands**, plain-text instructions that predate
the smartphone by decades and are still exactly how you register on a network, configure data, send an
SMS, or dial a call from first principles. You'll practice the actual command sequences in the AT
Command Console tab before you're troubleshooting a real modem over a serial link with no safety net.

## Prerequisites

| Requirement | Notes |
|---|---|
| **Cyberdeck-Build completed** | This project assumes a working cyberdeck and its power-budgeting skill already covered there |
| A modern browser | Chrome, Firefox, Safari, or Edge — the interactive tour is a single HTML file, no install |
| Python 3.8+ (for the exercises) | Check with `python3 --version` |
| Nothing else required to start | Real LTE hardware + an activated SIM only needed for the hardware appendix — see below before buying anything |

## Items Needed

Covered in the [Hardware Buying Guide](#hardware-buying-guide-what-to-look-for--red-flags) below with
tiered picks and links in the chain-wide [Hardware Shopping List](../HARDWARE_SHOPPING_LIST.md#cyberdeck-cellular-and-media):

- [ ] An LTE HAT or USB modem (SIM7600-class, confirm it supports your carrier's bands first)
- [ ] An activated SIM with a data plan
- [ ] **Both** main and diversity/MIMO antennas — not just one
- [ ] A USB or I2S audio interface + small speaker or headphone amp
- [ ] A USB power meter (reuse the one from Cyberdeck-Build's power budgeting)

## Quick Start

1. **Open the interactive tour.** Double-click `docs/interactive/index.html` — no server, no build step.
2. **Work Lesson 1 (Modems & AT commands) first**, then open the **AT Command Console** tab and work
   through Scenario 1 (check signal + registration).
   > ⚠️ **You may get stuck here:** the console checks your typed command against an exact expected
   > string. If it says "not quite," click **Hint** — it shows the exact AT command for that step.
3. **Work Lesson 2 (APN)**, then Console Scenario 2 (configure APN, verify data attach).
4. **Work Lesson 3 (SMS & voice)**, then Console Scenarios 3 and 4. Scenario 3's last step is
   **freeform** — after `AT+CMGF=1` and `AT+CMGS="..."`, type any message text; that step isn't checking
   an exact string, it's simulating the modem waiting for your message body.
5. **Do the skeleton-code exercise.**
   ```bash
   cd exercises
   python3 -m venv .venv && source .venv/bin/activate
   pip install pytest
   pytest -v
   ```
   You'll see 12 failing tests. Open `exercises/at_response_parser.py` and implement the four functions
   — full instructions in [`exercises/README.md`](exercises/README.md).
6. **Work Lesson 4 (audio & power)**, then the Quiz, then Flashcards/Match/Pop Quiz for review.
   > ⚠️ **You may get stuck here:** if real hardware resets specifically when sending an SMS or placing
   > a call, that's almost always a power-supply sizing problem (see Lesson 4), not a modem or SIM fault.
7. **Check the Report Card tab** any time. Click **Print / Save as PDF** to keep a dated copy in `docs/`.

## Exercise Overview

| # | Lesson | Concept | AT Command Console scenario |
|---|---|---|---|
| 1 | Modems & AT commands | Serial ports, AT basics, registration status | Scenario 1 — Check signal & registration |
| 2 | APN & carrier auth | Registration vs data, APN config, antennas | Scenario 2 — APN & data |
| 3 | SMS & voice | Text vs PDU mode, sending SMS, dialing/hanging up | Scenarios 3 & 4 — Send an SMS / Voice call |
| 4 | Audio & power | ALSA/PulseAudio, ground-loop noise, transmit-burst current | *(hardware appendix — measure with a USB power meter; see `exercises/`)* |

**Learning path:**
```
Lesson 1 (AT basics)  →  Lesson 2 (APN)  →  Lesson 3 (SMS & voice)  →  Lesson 4 (audio & power)
        ↓                                          ↓
AT Command Console: Scenarios 1-2         Scenarios 3-4 + exercises/ (at_response_parser.py)
        ↓
   Quiz → Flashcards/Match/Pop Quiz → Report Card
```

## Hardware Buying Guide (what to look for & red flags)

**Parts list:** an LTE HAT or USB modem (SIM7600-class modules are well documented), an activated SIM
with a data plan, antennas for the correct bands, a USB or I2S audio interface, and a small speaker or
headphone amp.

**What to look for:** check that the module supports the LTE bands your carrier actually uses in your
region — a module that works fine in one country may not attach at all in another. Prefer modules with
published AT-command documentation and active community support, and confirm the antenna connector type
before ordering.

**Red flags:** modems advertised as "universal" with no band list, kits shipped without antennas (they
will barely attach without them), and unlocked-claims on carrier-locked hardware. Very cheap audio HATs
often introduce persistent electrical noise.

**Common failure points:** insufficient power during transmit bursts causing resets, missing or
wrong-band antennas, APN misconfiguration preventing data, and ground-loop noise in the audio path.

## Why This Matters (Industry Application)

Cellular connectivity is the backbone of IoT and edge deployments, where wifi isn't available. Working
with modems and audio hardware means dealing with drivers and hardware interfaces directly, which is a
different and useful kind of debugging.

## How This Connects

Chain K (Hardware & Systems Foundations). Extends **Cyberdeck-Build**; the network layer connects to
**Home-Networking-And-Firewalls**.

## Project Layout

```
Cyberdeck-Cellular-And-Media/
├── docs/
│   ├── interactive/index.html   # tour: lessons, quiz, flashcards, match, pop quiz, AT console, report card
│   ├── LESSON_PLAN.md           # short build-plan reference
│   ├── LESSON.pdf               # the full written lesson, printable
│   ├── CHEATSHEET.pdf           # one-page command/rule recap, printable
│   └── RESOURCES.pdf            # further-reading links, printable
├── exercises/
│   ├── at_response_parser.py    # skeleton — implement the 4 functions
│   ├── test_at_response_parser.py
│   └── README.md
└── README.md                    # this file
```

---
Dual licensed — [GPL v3](LICENSE-GPL) and [AGPL v3](LICENSE-AGPL).
