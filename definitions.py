import os

# PATHS
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SOURCE = os.path.join(ROOT_DIR, 'static', 'payments_configuration.txt')

# GROUP NAMES FOR REGEX
WEEKDAYS_GROUP = 'weekdays'
WEEKENDS_GROUP = 'weekends'
INITIAL = 'initial'
END = 'end'
AMOUNT = 'amount'
NAME = 'name'
HOURS = 'hours'
MINUTES = 'minutes'
DAY = 'day'

# REGEX
CONFIG_REGEX = 'Monday.*Friday\n*(?P<%s>(.*USD\s*)*)Saturday.*Sunday\n*(?P<%s>(.*USD\s*)*)' % (
    WEEKDAYS_GROUP, WEEKENDS_GROUP)
CONFIG_ENTRY_REGEX = '(?P<%s>\d{2}:\d{2})\s*-*\s*(?P<%s>\d{2}:\d{2})\s*(?P<%s>\d+)\s*USD' % (INITIAL, END, AMOUNT)

QUESTION_REGEX = '(?P<%s>\w+)=(?P<%s>.*)' % (NAME, HOURS)
QUESTION_ITEM_SEPARATOR = ','

QUESTION_HOUR_ITEM_REGEX = '(?P<%s>\w{2})(?P<%s>\d{2}:\d{2})-(?P<%s>\d{2}:\d{2})' % (DAY, INITIAL, END)
TIME_REGEX = '^(?P<%s>\d{2}):(?P<%s>\d{2})$' % (HOURS, MINUTES)

# CONFIGS
WEEKDAYS = ['MO', 'TU', 'WE', 'TH', 'FR']
WEEKENDS = ['SA', 'SU']
