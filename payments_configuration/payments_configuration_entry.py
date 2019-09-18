import re

from custom_exceptions import ValidationException

TIME_REGEX = '^(?P<hour>\d{2}):(?P<minutes>\d{2})$'


class PaymentsConfigurationEntry:

    def __init__(self, initial_time, end_time, value):
        PaymentsConfigurationEntry.validate_time('initial_time', initial_time)
        PaymentsConfigurationEntry.validate_time('end_time', end_time)
        self.initial_time = initial_time
        self.end_time = end_time
        self.value = value

    @staticmethod
    def validate_time(field, time):
        expression_matching = re.match(TIME_REGEX, time)
        if not expression_matching or not int(expression_matching.group("hour")) in range(0, 24) or not int(
                expression_matching.group("minutes")) in range(0, 60):
            raise ValidationException(field)
