import pytest
import datetime
from snekdate.snekdate import SnekDate


############offset
def test_offset_type_returned():
    assert isinstance(SnekDate().offset(days=1), SnekDate)


@pytest.mark.parametrize(
    'end_date,offset_date,days,hours,minutes,seconds',
    [
        (
                datetime.datetime(day=20, year=2020, month=7),
                datetime.datetime(day=19, year=2020, month=7),
                1,
                0,
                0,
                0,
        ),
        (
                datetime.datetime(day=20, year=2020, month=7, hour=4, minute=5, second=20),
                datetime.datetime(day=20, year=2020, month=7, hour=4, minute=5, second=15),
                0,
                0,
                0,
                5,
        ),
        (
                datetime.datetime(day=20, year=2020, month=7, hour=4, minute=5, second=20),
                datetime.datetime(day=20, year=2020, month=7, hour=4, minute=3, second=50),
                0,
                0,
                0,
                90,
        ),
    ]
)
def test_offset_value_returned(end_date, offset_date, days, hours, minutes, seconds):
    assert SnekDate(end_date).offset(
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
    ).start == offset_date


############round_down_date
def test_round_down_type_returned():
    assert isinstance(SnekDate().round_down(increment='minute').start, datetime.datetime)


def test_round_down_exception():
    with pytest.raises(Exception):
        SnekDate.round_down_date(SnekDate().round_down(increment='minute'), increment='min')

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
def test_round_down_value_returned(date_raw, date_rounded, increment):
    assert SnekDate(date_raw).round_down(increment=increment).start == date_rounded
