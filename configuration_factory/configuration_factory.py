import re, os
from definitions import ROOT_DIR
from payments_configuration.payments_configuration import PaymentsConfiguration

DEFAULT_SOURCE = os.path.join(ROOT_DIR, 'static', 'payments_configuration.txt')
CONFIG_REGEX = 'Monday.*Friday\n*(?P<weekdays>(.*USD\s*)*)Saturday.*Sunday\n*(?P<weekends>(.*USD\s*)*)'


class ConfigurationFactory:

    def __init__(self):
        pass

    @staticmethod
    def build(input_file=DEFAULT_SOURCE):
        input_file = input_file if input_file else DEFAULT_SOURCE
        my_file = open(input_file, "r")
        matches = re.match(CONFIG_REGEX, ''.join(my_file.readlines()))
        my_file.close()
        return PaymentsConfiguration(matches.group('weekdays'), matches.group('weekends'))
