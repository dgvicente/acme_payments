import re
from custom_exceptions import ValidationException
from .day_time import DayTime

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

    @staticmethod
    def validate_number(field, value):
        try:
            int(value)
        except ValueError:
            raise ValidationException(field)
