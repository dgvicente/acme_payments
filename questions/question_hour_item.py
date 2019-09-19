import re

from common.day_time import DayTime

QUESTION_HOUR_ITEM_REGEX = '(?P<day>\w{2})(?P<initial>\d{2}:\d{2})-(?P<end>\d{2}:\d{2})'
WEEKDAYS = ['MO', 'TU', 'WE', 'TH', 'FR']
WEEKENDS = ['SA', 'SU']


class QuestionHourItem:

    def __init__(self, raw_item):
        matches = re.match(QUESTION_HOUR_ITEM_REGEX, raw_item)
        self.day_of_week = matches.group('day')
        self.initial_time = DayTime(matches.group('initial'))
        self.end_time = DayTime(matches.group('end'))

    def is_weekday(self):
        return self.day_of_week in WEEKDAYS


