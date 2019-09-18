import re
from custom_exceptions import ValidationException

TIME_REGEX = '^(?P<hour>\d{2}):(?P<minutes>\d{2})$'
MIDNIGHT = 0


class DayTime:

    def __init__(self, value):
        matched_time = re.match(TIME_REGEX, value)
        if not matched_time:
            raise ValidationException()
        self.hours = int(matched_time.group('hour'))
        self.minutes = int(matched_time.group('minutes'))

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
