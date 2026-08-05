# Cyberdeck-Cellular-And-Media

### Add cellular calling, SMS texting, and music playback to the cyberdeck (LTE HAT + audio) — effectively a DIY phone.

![Chain K](https://img.shields.io/badge/Chain%20K-64748B?style=for-the-badge) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE-GPL) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue?style=for-the-badge)](LICENSE-AGPL)

[📖 Lesson Plan](docs/LESSON_PLAN.md)

<!-- SCREENSHOT PLACEHOLDER: docs/screenshots/overview.png -->

> ⬜ **Scaffold pending.** Directory created to portfolio standard; full content to be built. Real-hardware build with an emulation/planning-first path. Part of **Chain K — Hardware & Systems Foundations**.

## Why This Was Built

Adding cellular and audio turns the cyberdeck from a portable computer into something genuinely independent
— it can connect without wifi and act as a communication device rather than just a terminal.

Cellular is the interesting part. An LTE HAT with a SIM means understanding modems, AT commands, and how a
mobile network authenticates a device — a layer of the stack I otherwise never touch.

## Hardware Buying Guide (What to look for & red flags)

**Parts list:** an LTE HAT or USB modem (SIM7600-class modules are well documented), an activated SIM with a
data plan, antennas for the correct bands, a USB or I2S audio interface, and a small speaker or headphone
amp.

**What to look for:** check that the module supports the LTE bands your carrier actually uses in your
region — a module that works fine in one country may not attach at all in another. Prefer modules with
published AT-command documentation and active community support, and confirm the antenna connector type
before ordering.

**Red flags:** modems advertised as "universal" with no band list, kits shipped without antennas (they will
barely attach without them), and unlocked-claims on carrier-locked hardware. Very cheap audio HATs often
introduce persistent electrical noise.

**Common failure points:** insufficient power during transmit bursts causing resets, missing or wrong-band
antennas, APN misconfiguration preventing data, and ground-loop noise in the audio path.

## Why This Matters (Industry Application)

Cellular connectivity is the backbone of IoT and edge deployments, where wifi isn't available. Working
with modems and audio hardware means dealing with drivers and hardware interfaces directly, which is a
different and useful kind of debugging.

## Topics Covered

| Area | What this project covers |
|------|--------------------------|
| LTE HAT | Adding a cellular modem to a single-board computer |
| Modems | AT commands and the interface to the network |
| SIM & carriers | Authentication, APNs, bands, and data plans |
| Calls & SMS | Voice and messaging through the modem |
| Audio | Playback, mixing, and audio hardware on Linux |
| Power | What always-on cellular costs the battery |

## How This Connects

Chain K (Hardware & Systems Foundations). Extends **Cyberdeck-Build**; the network layer connects to **Home-Networking-And-Firewalls**.

---
Dual licensed — [GPL v3](LICENSE-GPL) and [AGPL v3](LICENSE-AGPL).
