import unittest

from questions.question import Question
from questions.questions_factory import QuestionsFactory
from mock import patch, MagicMock

from tests.helpers import random_string


class TestQuestionsFactory(unittest.TestCase):

    def test_should_return_a_list_of_questions_using_default_file(self):
        questions = QuestionsFactory.build()
        self.assertEqual(len(questions), 4)
        self.assertIsInstance(questions[0], Question)

    def test_should_return_a_list_of_questions_using_default_file_when_provided_file_is_none(self):
        questions = QuestionsFactory.build(None)
        self.assertEqual(len(questions), 4)
        self.assertIsInstance(questions[0], Question)

    @patch("builtins.open")
    def test_should_build_configuration_using_given_file_when_is_provided(self, mock_open):
        expected_file_name = random_string(20)
        file_pointer = MagicMock()
        file_pointer.readlines.return_value = ['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00']
        mock_open.return_value = file_pointer

        QuestionsFactory.build(expected_file_name)

        mock_open.assert_called_with(expected_file_name, 'r')
