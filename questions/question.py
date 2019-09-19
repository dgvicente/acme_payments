import re
from definitions import QUESTION_REGEX, QUESTION_ITEM_SEPARATOR, NAME, HOURS
from questions.question_hour_item import QuestionHourItem


class Question:
    def __init__(self, raw_question):
        matches = re.match(QUESTION_REGEX, raw_question)
        self.name = matches.group(NAME)
        self.items = [QuestionHourItem(item) for item in matches.group(HOURS).split(QUESTION_ITEM_SEPARATOR) if item]
