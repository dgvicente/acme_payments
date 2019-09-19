import random
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

    def test_is_weekday_should_return_true_if_it_is_associated_to_day_from_monday_to_friday(self):
        weekday = random.choice(['MO', 'TU', 'WE', 'TH', 'FR'])
        question_hour_item = QuestionHourItem('%s10:00-12:00' % weekday)

        self.assertTrue(question_hour_item.is_weekday())

    def test_is_weekday_should_return_false_if_it_is_associated_to_saturday_or_sunday(self):
        weekday = random.choice(['SA', 'SU'])
        question_hour_item = QuestionHourItem('%s10:00-12:00' % weekday)

        self.assertFalse(question_hour_item.is_weekday())

    def test_should_given_regex_when_provided(self):
        pattern = '(?P<day>\w{2}).*\s+from\s+(?P<initial>\d{2}:\d{2})\s+to\s+(?P<end>\d{2}:\d{2})'
        question_hour_item = QuestionHourItem('MONDAY from 10:00 to 12:00', pattern)

        self.assertEqual(question_hour_item.day_of_week, 'MO')
        self.assertEqual(question_hour_item.initial_time, DayTime('10:00'))
        self.assertEqual(question_hour_item.end_time, DayTime('12:00'))
