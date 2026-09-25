# Exercises — AT Response Parser

A hands-on companion to Lessons 1 and 3 in the interactive tour. Sending an AT command is the easy
half of modem control — parsing what it replies is the half you actually need for a real script. These
functions use the same response formats the AT Command Console tab scripts.

## Setup

```bash
# from this exercises/ folder
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pytest
```

## Run the tests

```bash
pytest -v
```

You'll see 12 failing tests — every function in `at_response_parser.py` currently raises
`NotImplementedError`.

## What to do

Open `at_response_parser.py`. Implement in this order:

1. `csq_to_dbm` — convert a raw CSQ value (0-31, or 99 for unknown) to an approximate dBm signal
   strength using the standard `-113 + 2*csq` formula.
2. `parse_creg` — extract the (mode, status) pair out of a `+CREG:` response line.
3. `is_registered` — given a status code from `parse_creg`, decide true/false registration.
4. `parse_cmgs_response` — extract the message reference number from a `+CMGS:` response.

Check each result against the AT Command Console tab's scripted responses as you go — Scenario 1 uses
the exact `+CSQ`/`+CREG` values these tests check against, and Scenario 3 uses the exact `+CMGS` value.

## When you're done

All 12 tests passing means you can turn raw modem replies into data a real script can act on — which is
most of what "controlling a modem" actually is, beyond knowing which command string to send.
