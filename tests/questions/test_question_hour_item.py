import unittest

from common.day_time import DayTime
from questions.question_hour_item import QuestionHourItem


class TestQuestionHourItem(unittest.TestCase):

    def test_should_create_a_question_hour_item_given_raw_info(self):
        raw_info = 'MO10:00-12:00'

        question_hour_item = QuestionHourItem(raw_info)

        self.assertEqual(question_hour_item.day_of_week, 'MO')
        self.assertEqual(question_hour_item.initial_time, DayTime('10:00'))
        self.assertEqual(question_hour_item.end_time, DayTime('12:00'))