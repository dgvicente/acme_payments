import re

from questions.question_hour_item import QuestionHourItem

QUESTION_REGEX = '(?P<name>\w+)=(?P<hours>.*)'


class Question:
    def __init__(self, raw_question):
        matches = re.match(QUESTION_REGEX, raw_question)
        self.name = matches.group('name')
        self.items = [QuestionHourItem(item) for item in matches.group('hours').split(',') if item]
