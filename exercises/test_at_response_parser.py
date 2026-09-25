"""
Tests for at_response_parser.py. Every expected value matches a docstring
example or the AT Command Console's scripted responses in the interactive
tour.
"""
import pytest

from at_response_parser import (
    csq_to_dbm,
    parse_creg,
    is_registered,
    parse_cmgs_response,
)


def test_csq_to_dbm_matches_console_scenario_1():
    # The AT Command Console's Scenario 1 returns +CSQ: 22,99
    assert csq_to_dbm(22) == -69


def test_csq_to_dbm_zero_is_worst_case():
    assert csq_to_dbm(0) == -113


def test_csq_to_dbm_max_value():
    assert csq_to_dbm(31) == -51


def test_csq_to_dbm_99_is_unknown():
    assert csq_to_dbm(99) is None


def test_parse_creg_matches_console_scenario_1():
    # The AT Command Console's Scenario 1 returns +CREG: 0,1
    assert parse_creg("+CREG: 0,1") == (0, 1)


def test_parse_creg_roaming():
    assert parse_creg("+CREG: 2,5") == (2, 5)


def test_is_registered_home_network():
    assert is_registered(1) is True


def test_is_registered_roaming():
    assert is_registered(5) is True


def test_is_registered_not_registered():
    assert is_registered(0) is False


def test_is_registered_searching():
    assert is_registered(2) is False


def test_parse_cmgs_response_matches_console_scenario_3():
    # The AT Command Console's Scenario 3 returns +CMGS: 12
    assert parse_cmgs_response("+CMGS: 12") == 12


def test_parse_cmgs_response_single_digit():
    assert parse_cmgs_response("+CMGS: 7") == 7
