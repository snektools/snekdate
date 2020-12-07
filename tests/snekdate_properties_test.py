import pytest
import datetime
from snekdate.snekdate import SnekDate

def test_start_type():
    assert isinstance(SnekDate().start, datetime.datetime)


def test_end_type():
    assert isinstance(SnekDate().offset().end, datetime.datetime)


def test_end_value_none():
    assert SnekDate().end is None


def test_start_end_value():
    sd = SnekDate().offset(days=1)
    assert sd.start < sd.end


def test_start_str_type():
    assert isinstance(SnekDate().offset(days=1).start_str, str)


def test_end_str_type():
    assert isinstance(SnekDate().offset(days=1).end_str, str)


def test_end_str_value_none():
    assert SnekDate().end_str is None


def test_range_type():
    sd_range = SnekDate().offset(days=1).range
    assert isinstance(sd_range, tuple) and all(isinstance(date, datetime.datetime) for date in sd_range)


def test_range_str_type():
    sd_range = SnekDate().offset(days=1).range_str
    assert isinstance(sd_range, tuple) and all(isinstance(date, str) for date in sd_range)


def test_range_values():
    sd_range = SnekDate().offset(days=1).range
    assert sd_range[0] < sd_range[1]