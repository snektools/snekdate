import datetime


def now() -> datetime.datetime:
    """
    A simple function to return the current time
    :return: The current time as a datetime object
    """
    return datetime.datetime.now()


def offset(
        date: datetime.datetime,
        backwards: bool = True,
        weeks: float = 0,
        days: float = 0.5,
        hours: float = 0,
        minutes: float = 0,
        seconds: float = 0,
) -> datetime.datetime:
    """
    This function will offset a date by the specified amount, which will help define the other end of the range.
    :param date: The original date to be offset from
    :param backwards: If this value is true, you will go back in time by the specified amount.
    :param weeks: Offset in weeks, total value is an accumulation of all arguments.
    :param days: Offset in days, total value is an accumulation of all arguments.
    :param hours: Offset in hours, total value is an accumulation of all arguments.
    :param minutes: Offset in minutes, total value is an accumulation of all arguments.
    :param seconds: Offset in seconds, total value is an accumulation of all arguments.
    :return: A datetime object that is offset from the original datetime.
    """
    print(days)
    delta = datetime.timedelta(
        weeks=weeks,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
    )
    if backwards:
        delta *= -1
    return date + delta


def round_down(
        time: datetime.datetime,
        increment: str = 'minute',
) -> datetime.datetime:
    """
    This is a simple function that rounds down to the nearest increment provided
    :param time: The original datetime object that will be rounded down.
    :param increment: The string of an the time to round down (ie minute)
    :return: A datetime object that is rounded down to the nearest time value.
    """
    allowed_values = ['microsecond','second','minute','hour','day','week']
    if not isinstance(increment, str) or increment.lower() not in allowed_values:
        raise Exception(f"""
        Value passed ({increment}) for increment was not valid. 
        Should be a string and one of the following values:
        {', '.join(allowed_values)}"""
                        )
    time_parameters = {}
    for allowed_value in allowed_values:
        if allowed_value==increment.lower():
            break
        time_parameters.update(
            {
                allowed_value:0
            }
        )
    return time.replace(**time_parameters)



def within(
        time1: datetime.datetime,
        time2: datetime.datetime,
        weeks: float = 0,
        days: float = 0,
        hours: float = 0,
        minutes: float = 0,
        seconds: float = 0,
) -> bool:
    delta = datetime.timedelta(
        weeks=weeks,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
    )

    return abs(time1 - time2) < delta


def to_str(date: datetime.datetime) -> str:
    if isinstance(date, str):
        return date
    else:
        return date.strftime('%Y-%m-%d %H:%M:%S')


def to_datetime(date: str) -> datetime.datetime:
    if isinstance(date, datetime.datetime):
        return date
    else:
        return datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
