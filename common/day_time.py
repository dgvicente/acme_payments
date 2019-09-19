import re
from custom_exceptions import ValidationException
from definitions import HOURS, TIME_REGEX, MINUTES

MIDNIGHT = 0


class DayTime:

    def __init__(self, value, pattern=TIME_REGEX):
        pattern = pattern if pattern else TIME_REGEX
        matched_time = re.match(pattern, value)
        if not matched_time:
            raise ValidationException()
        self.hours = int(matched_time.group(HOURS))
        self.minutes = int(matched_time.group(MINUTES))

    @staticmethod
    def from_values(hours, minutes):
        hour = str(hours).zfill(2)
        minutes = str(minutes).zfill(2)
        return DayTime('%s:%s' % (hour, minutes))

    def __eq__(self, other):
        if isinstance(other, DayTime):
            return other.hours == self.hours and other.minutes == self.minutes
        return False

    def __lt__(self, other):
        top_hour = 24 if self.hours == 0 and self.minutes == 0 else self.hours
        bottom_hour = 24 if other.hours == 0 and other.minutes == 0 else other.hours
        return top_hour < bottom_hour or (top_hour == bottom_hour and self.minutes <= other.minutes)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __add__(self, other):
        hour = str(self.hours + other.hours).zfill(2)
        minutes = str(self.minutes + other.minutes).zfill(2)
        return DayTime('%s:%s' % (hour, minutes))

    def __sub__(self, other):
        initial = self._hours_to_midnight(self.hours) * 60 + self.minutes
        end = other.hours * 60 + other.minutes
        return (initial - end)/60

    def __str__(self):
        hour = str(self.hours).zfill(2)
        minutes = str(self.minutes).zfill(2)
        return '%s:%s' % (hour, minutes)

    @staticmethod
    def _hours_to_midnight(hours):
        return hours if hours != 0 else 24

