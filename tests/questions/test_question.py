import unittest

from questions.question import Question
from questions.question_hour_item import QuestionHourItem


class TestQuestion(unittest.TestCase):

    def test_should_create_a_question_given_a_raw_info(self):
        raw_info = 'RENE=MO10:00-12:00,TU10:00-12:00'
        question = Question(raw_info)
        self.assertEqual(question.name, 'RENE')
        self.assertEqual(len(question.items), 2)
        self.assertIsInstance(question.items[0], QuestionHourItem)
