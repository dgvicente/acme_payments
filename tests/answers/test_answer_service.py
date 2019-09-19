import unittest
from mock import MagicMock
from answers.answer import Answer
from answers.answers_service import AnswersService
from questions.question import Question


class TestAnswerService(unittest.TestCase):

    def test_should_provide_an_answer_for_every_question(self):
        questions = [Question('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')]
        payment_configuration = MagicMock()

        answers_service = AnswersService(payment_configuration, questions)
        answers = answers_service.answer()

        self.assertEqual(len(questions), len(answers))
        self.assertIsInstance(answers[0], Answer)
