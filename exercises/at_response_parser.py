"""
AT Response Parser — fill in the four functions below.

A real modem-control script doesn't just send AT commands (that part's easy,
it's a string) — it has to parse the modem's replies back into something a
program can act on. These four functions are exactly that: the same parsing
you'd write for a real SIM7600-class integration, using the same response
formats covered in the interactive tour's lessons and AT Command Console.

Run the tests as you go:  pytest exercises/test_at_response_parser.py -v
All four start failing. Implement one function, re-run, watch it turn green,
move to the next.
"""


def csq_to_dbm(csq):
    """Convert a CSQ signal-quality value (0-31, or 99 for unknown) to an
    approximate signal strength in dBm.

    The standard conversion (used across SIMCom/Quectel-class modems) is:
    dBm = -113 + 2 * csq, valid for csq 0-31. csq == 99 means "not known or
    not detectable" and has no dBm equivalent — return None for that case.

    >>> csq_to_dbm(22)
    -69
    >>> csq_to_dbm(0)
    -113
    >>> csq_to_dbm(99) is None
    True
    """
    # TODO: apply the formula above for csq 0-31, return None for csq == 99
    raise NotImplementedError


def parse_creg(response):
    """Parse a +CREG response line into (mode, status) as a tuple of ints.

    The tour's AT Command Console returns lines like "+CREG: 0,1" — the
    first number is the unsolicited-result-code mode (usually 0 or 2,
    not what you care about here), the second is what Lesson 1 covers:
    registration status.

    >>> parse_creg("+CREG: 0,1")
    (0, 1)
    >>> parse_creg("+CREG: 2,5")
    (2, 5)
    """
    # TODO: extract the two comma-separated integers after "+CREG: "
    raise NotImplementedError


def is_registered(creg_status):
    """Given just the status field from parse_creg(), return True if the
    modem is registered (home network or roaming), False otherwise.

    Per Lesson 1: 1 = registered, home network. 5 = registered, roaming.
    0, 2, 3, 4 all mean "not registered" in one way or another (not
    searching, searching, denied, unknown).

    >>> is_registered(1)
    True
    >>> is_registered(5)
    True
    >>> is_registered(0)
    False
    """
    # TODO: return True only for status 1 or 5
    raise NotImplementedError


def parse_cmgs_response(response):
    """Parse a +CMGS response line into the message reference number.

    After a successful AT+CMGS send (Lesson 3), the modem replies with
    something like "+CMGS: 12" — the number is a reference ID for that
    specific sent message, useful for correlating delivery reports later.

    >>> parse_cmgs_response("+CMGS: 12")
    12
    >>> parse_cmgs_response("+CMGS: 7")
    7
    """
    # TODO: extract and return the integer after "+CMGS: "
    raise NotImplementedError
