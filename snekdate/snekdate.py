import datetime


class SnekDate:
    def __init__(self, date=None, other_date=None):
        if date:
            self._this_date = self.to_datetime(date)
        else:
            self._this_date = self.now()

        self._other_date = other_date

    def offset(
            self,
            backwards: bool = True,
            weeks: float = 0,
            days: float = 0,
            hours: float = 0,
            minutes: float = 0,
            seconds: float = 0,
    ):
        """
        This method will offset a date by the specified amount, which will help define the other end of the range.
        :param date: The original date to be offset from
        :param backwards: If this value is true, you will go back in time by the specified amount.
        :param weeks: Offset in weeks, total value is an accumulation of all arguments.
        :param days: Offset in days, total value is an accumulation of all arguments.
        :param hours: Offset in hours, total value is an accumulation of all arguments.
        :param minutes: Offset in minutes, total value is an accumulation of all arguments.
        :param seconds: Offset in seconds, total value is an accumulation of all arguments.
        :return: A new SnekDate object with the updated dates.
        """
        delta = datetime.timedelta(
            weeks=weeks,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds,
        )
        if backwards:
            delta *= -1
        return SnekDate(date=self._this_date, other_date=self._this_date + delta)

    def round_down(
            self,
            increment: str = 'minute'
    ):
        """
        This method will round down both dates using the static method
        :param time: The original datetime object that will be rounded down.
        :param increment: The string of an the time to round down (ie minute)
        :return: A a new SnekDate object.
        """
        if self._other_date:
            other_date = self.round_down_date(self._other_date, increment=increment)
        else:
            other_date = self._other_date
        return SnekDate(
            date=self.round_down_date(self._this_date, increment=increment),
            other_date= other_date,
        )


    @staticmethod
    def round_down_date(
            time: datetime.datetime,
            increment: str = 'minute',
    ) -> datetime.datetime:
        """
        This is a simple function that rounds down to the nearest increment provided
        :param time: The original datetime object that will be rounded down.
        :param increment: The string of an the time to round down (ie minute)
        :return: A datetime object that is rounded down to the nearest time value.
        """
        allowed_values = ['microsecond', 'second', 'minute', 'hour', 'day', 'week']
        if not isinstance(increment, str) or increment.lower() not in allowed_values:
            raise Exception(f"""
            Value passed ({increment}) for increment was not valid. 
            Should be a string and one of the following values:
            {', '.join(allowed_values)}"""
                            )
        time_parameters = {}
        for allowed_value in allowed_values:
            if allowed_value == increment.lower():
                break
            time_parameters.update(
                {
                    allowed_value: 0
                }
            )
        return time.replace(**time_parameters)

    @staticmethod
    def now() -> datetime.datetime:
        """
        A simple function to return the current time
        :return: The current time as a datetime object
        """
        return datetime.datetime.now()

    @staticmethod
    def to_str(date: datetime.datetime) -> str:
        if isinstance(date, str):
            return date
        else:
            return date.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def to_datetime(date: str) -> datetime.datetime:
        if isinstance(date, datetime.datetime):
            return date
        else:
            return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

    @property
    def start(self):
        if not self._other_date:
            return self._this_date
        return min([self._this_date, self._other_date])

    @property
    def end(self):
        if self._other_date:
            return max([self._this_date, self._other_date])

    @property
    def start_str(self):
        if not self._other_date:
            return self.to_str(self._this_date)
        return self.to_str(min([self._this_date, self._other_date]))

    @property
    def end_str(self):
        if self._other_date:
            return self.to_str(max([self._this_date, self._other_date]))

    @property
    def range(self):
        if self._other_date:
            return tuple(sorted([self._this_date, self._other_date]))

    @property
    def range_str(self):
        if self._other_date:
            return tuple(sorted([self.to_str(self._this_date), self.to_str(self._other_date)]))

