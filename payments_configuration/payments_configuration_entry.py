import re
from custom_exceptions import ValidationException
from .day_time import DayTime

TIME_REGEX = '^(?P<hour>\d{2}):(?P<minutes>\d{2})$'


class PaymentsConfigurationEntry:

    def __init__(self, initial_time, end_time, value):
        PaymentsConfigurationEntry.validate_number('value', value)
        PaymentsConfigurationEntry.validate_hours_range(initial_time, end_time)
        self.initial_time = DayTime(initial_time)
        self.end_time = DayTime(end_time)
        self.value = value

    @staticmethod
    def validate_number(field, value):
        try:
            int(value)
        except ValueError:
            raise ValidationException(field)

    @staticmethod
    def validate_hours_range(initial_time, end_time):
        if initial_time == end_time or initial_time > end_time:
            raise ValidationException('hours range', initial_time, end_time)
