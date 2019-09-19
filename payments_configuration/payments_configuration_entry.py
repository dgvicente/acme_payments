import re
from custom_exceptions import ValidationException
from common.day_time import DayTime
from definitions import CONFIG_ENTRY_REGEX, INITIAL, END, AMOUNT


class PaymentsConfigurationEntry:

    def __init__(self, raw_value, pattern=None):
        pattern = pattern if pattern else CONFIG_ENTRY_REGEX
        matches = re.match(pattern, raw_value)
        if not matches:
            raise ValidationException('Wrong structure', raw_value)
        PaymentsConfigurationEntry.validate_number(AMOUNT, matches.group(AMOUNT))
        self.initial_time = DayTime(matches.group(INITIAL))
        self.end_time = DayTime(matches.group(END))
        self.validate_hours_range()
        self.amount = int(matches.group(AMOUNT))

    def validate_hours_range(self):
        if self.initial_time >= self.end_time:
            raise ValidationException('Invalid hours range', self.initial_time, self.end_time)

    def get_hours_contained(self, initial_time, end_time):
        one_minute = DayTime('00:01')
        initial_time = initial_time if initial_time + one_minute >= self.initial_time else \
            DayTime.from_values(self.initial_time.hours, self.initial_time.minutes - 1)
        end_time = end_time if end_time <= self.end_time else self.end_time
        return end_time - initial_time if end_time > initial_time + one_minute else 0

    @staticmethod
    def validate_number(field, value):
        try:
            int(value)
        except ValueError:
            raise ValidationException(field)
