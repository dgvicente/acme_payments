import re
from custom_exceptions import ValidationException
from common.day_time import DayTime

ENTRY_REGEX = '(?P<initial>\d{2}:\d{2})\s*-*\s*(?P<end>\d{2}:\d{2})\s*(?P<amount>\d+)\s*USD'


class PaymentsConfigurationEntry:

    def __init__(self, raw_value):
        matches = re.match(ENTRY_REGEX, raw_value)
        if not matches:
            raise ValidationException('Wrong structure', raw_value)
        PaymentsConfigurationEntry.validate_number('value', matches.group('amount'))
        self.initial_time = DayTime(matches.group('initial'))
        self.end_time = DayTime(matches.group('end'))
        self.validate_hours_range()
        self.value = int(matches.group('amount'))

    def validate_hours_range(self):
        if self.initial_time >= self.end_time:
            raise ValidationException('Invalid hours range', self.initial_time, self.end_time)

    def get_hours_contained(self, initial_time, end_time):
        one_minute = DayTime('00:01')
        initial_time = initial_time if initial_time + one_minute >= self.initial_time else \
            DayTime.from_values(self.initial_time.hours, self.initial_time.minutes - 1)
        end_time = end_time if end_time <= self.end_time else self.end_time
        return end_time - initial_time if end_time > initial_time else 0

    @staticmethod
    def validate_number(field, value):
        try:
            int(value)
        except ValueError:
            raise ValidationException(field)
