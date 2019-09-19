import unittest
from questions.question import Question
from questions.questions_factory import QuestionsFactory
from mock import patch, MagicMock
from tests.helpers import random_string


@patch("builtins.open")
class TestQuestionsFactory(unittest.TestCase):

    def setUp(self):
        self.file_pointer = MagicMock()
        self.file_pointer.readlines.return_value = ['RENE=MO10:00-12:00']

    def test_should_return_a_list_of_questions_using_default_file(self, mock_open):
        mock_open.return_value = self.file_pointer
        questions = QuestionsFactory.build()
        self.assertEqual(1, len(questions))
        self.assertIsInstance(questions[0], Question)

    def test_should_return_a_list_of_questions_using_default_file_when_provided_file_is_none(self, mock_open):
        mock_open.return_value = self.file_pointer
        questions = QuestionsFactory.build(None)
        self.assertEqual(1, len(questions))
        self.assertIsInstance(questions[0], Question)

    def test_should_build_configuration_using_given_file_when_is_provided(self, mock_open):
        mock_open.return_value = self.file_pointer
        expected_file_name = random_string(20)
        QuestionsFactory.build(expected_file_name)
        mock_open.assert_called_with(expected_file_name, 'r')
