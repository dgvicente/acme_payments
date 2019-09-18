from custom_exceptions import ValidationException
from .day_time import DayTime

TIME_REGEX = '^(?P<hour>\d{2}):(?P<minutes>\d{2})$'


class PaymentsConfigurationEntry:

    def __init__(self, initial_time, end_time, value):
        PaymentsConfigurationEntry.validate_number('value', value)
        self.initial_time = DayTime(initial_time)
        self.end_time = DayTime(end_time)
        self.validate_hours_range()
        self.value = int(value)

    def validate_hours_range(self):
        if self.initial_time >= self.end_time:
            raise ValidationException('Invalid hours range', self.initial_time, self.end_time)

    @staticmethod
    def validate_number(field, value):
        try:
            int(value)
        except ValueError:
            raise ValidationException(field)
