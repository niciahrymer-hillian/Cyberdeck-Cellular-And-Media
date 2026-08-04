# 📖 Lesson Plan — Cyberdeck-Cellular-And-Media

> **Chain K — Hardware & Systems Foundations** | Add cellular calling, SMS texting, and music playback to the cyberdeck (LTE HAT + audio) — effectively a DIY phone.

## What This Project Is

Add LTE connectivity and audio to the cyberdeck — modems, AT commands, carrier attachment, and sound on Linux.

## Learning Objectives

By the end I can:

1. Attach an LTE modem and verify carrier registration.
2. Issue **AT commands** and interpret the responses.
3. Configure APN settings for a data connection.
4. Send and receive SMS, and place a call, through the modem.
5. Configure Linux audio for playback and capture.
6. Measure what always-on cellular costs the battery.

## Software You Will Use

- A SIM7600-class LTE HAT or USB modem.
- ModemManager / mmcli.
- minicom or screen for AT commands.
- ALSA/PulseAudio.

## Build Order

1. Confirm band compatibility with your carrier before anything else.
2. Attach the modem; verify registration with AT commands.
3. Configure the APN and establish a data connection.
4. Test SMS and voice.
5. Configure audio output and test playback.
6. Measure battery impact with the modem active.

## Common Mistakes to Avoid

- Buying a module that does not support your carrier's bands.
- Running without antennas and blaming the module.
- Insufficient power during transmit bursts causing resets.
- Wrong APN, so registration succeeds but data never works.
- Ground-loop noise from a cheap audio interface.

## Check Your Understanding

The quiz covers band compatibility, AT command basics, APN configuration, and power draw during transmit.

## Why This Matters (Industry Application)

Cellular connectivity is the backbone of IoT and edge deployments, where wifi isn't available. Working
with modems and audio hardware means dealing with drivers and hardware interfaces directly, which is a
different and useful kind of debugging.

## Reflection Questions

- What does having a device that works without wifi actually change about how you use it?
- Where would cellular-connected edge hardware genuinely be useful in your own domain?
