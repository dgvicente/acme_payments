import re
from common.day_time import DayTime
from definitions import QUESTION_HOUR_ITEM_REGEX, WEEKDAYS, DAY, INITIAL, END


class QuestionHourItem:

    def __init__(self, raw_item, pattern=QUESTION_HOUR_ITEM_REGEX):
        pattern = pattern if pattern else QUESTION_HOUR_ITEM_REGEX
        matches = re.match(pattern, raw_item)
        self.day_of_week = matches.group(DAY)
        self.initial_time = DayTime(matches.group(INITIAL))
        self.end_time = DayTime(matches.group(END))

    def is_weekday(self):
        return self.day_of_week in WEEKDAYS


