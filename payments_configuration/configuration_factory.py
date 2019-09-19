import re
from definitions import DEFAULT_SOURCE, CONFIG_REGEX, WEEKDAYS_GROUP, WEEKENDS_GROUP
from payments_configuration.payments_configuration import PaymentsConfiguration


class ConfigurationFactory:

    def __init__(self):
        pass

    @staticmethod
    def build(input_file=DEFAULT_SOURCE, pattern=CONFIG_REGEX):
        input_file = input_file if input_file else DEFAULT_SOURCE
        pattern = pattern if pattern else CONFIG_REGEX
        my_file = open(input_file, "r")
        matches = re.match(pattern, ''.join(my_file.readlines()))
        my_file.close()
        return PaymentsConfiguration(matches.group(WEEKDAYS_GROUP).split('\n'), matches.group(WEEKENDS_GROUP).split('\n'))
