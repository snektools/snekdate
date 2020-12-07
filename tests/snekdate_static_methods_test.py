import pytest
import datetime
from snekdate.snekdate import SnekDate


############round_down_date
def test_round_down_date_type_returned():
    assert isinstance(SnekDate.round_down_date(SnekDate.now(), increment='minute'), datetime.datetime)


def test_round_down_date_exception():
    with pytest.raises(Exception):
        SnekDate.round_down_date(SnekDate.now(), increment='min')

@pytest.mark.parametrize(
    'date_raw,date_rounded,increment',
    [
        (
                datetime.datetime(day=20, year=2020, month=7, hour=3, minute=5, second=15),
                datetime.datetime(day=20, year=2020, month=7, hour=3, minute=5, second=0),
                'minute',
        ),
        (
                datetime.datetime(day=20, year=2020, month=7, hour=3, minute=5, second=15),
                datetime.datetime(day=20, year=2020, month=7, hour=3, minute=0, second=0),
                'hour',
        ),
        (
                datetime.datetime(day=20, year=2020, month=7, hour=3, minute=5, second=15),
                datetime.datetime(day=20, year=2020, month=7, hour=0, minute=0, second=0),
                'day',
        ),
    ]
)
def test_round_down_date_value_returned(date_raw, date_rounded, increment):
    assert SnekDate.round_down_date(time=date_raw, increment=increment) == date_rounded


############now
def test_now_type_returned():
    assert type(SnekDate.now()) == datetime.datetime



############datetime_to_str
def test_to_str_type_returned():
    assert isinstance(SnekDate.to_str(datetime.datetime(day=20, year=2020, month=7)), str)


@pytest.mark.parametrize(
    'date,string',
    [
        (datetime.datetime(day=20, year=2020, month=7), '2020-07-20 00:00:00'),
        (datetime.datetime(day=1, year=2001, month=12), '2001-12-01 00:00:00'),
        (datetime.datetime(day=20, year=2020, month=7, hour=3), '2020-07-20 03:00:00'),
        (datetime.datetime(day=20, year=2020, month=7, hour=3, minute=1), '2020-07-20 03:01:00'),
        (datetime.datetime(day=20, year=2020, month=7, hour=3, minute=5, second=15), '2020-07-20 03:05:15'),
    ]
)
def test_to_str_value_returned(date, string):
    assert SnekDate.to_str(date) == string


############str_to_datetime
def test_to_date_type_returned():
    assert isinstance(SnekDate.to_datetime('2020-07-20 00:00:00'), datetime.datetime)


@pytest.mark.parametrize(
    'date,string',
    [
        (datetime.datetime(day=20, year=2020, month=7), '2020-07-20 00:00:00'),
        (datetime.datetime(day=1, year=2001, month=12), '2001-12-01 00:00:00'),
        (datetime.datetime(day=20, year=2020, month=7, hour=3), '2020-07-20 03:00:00'),
        (datetime.datetime(day=20, year=2020, month=7, hour=3, minute=1), '2020-07-20 03:01:00'),
        (datetime.datetime(day=20, year=2020, month=7, hour=3, minute=5, second=15), '2020-07-20 03:05:15'),
    ]
)
def test_to_datetime_value_returned(date, string):
    assert SnekDate.to_datetime(string) == date