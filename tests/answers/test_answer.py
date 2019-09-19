import unittest
from answers.answer import Answer
from payments_configuration.configuration_factory import ConfigurationFactory
from questions.question import Question
from mock import patch, MagicMock


class TestAnswer(unittest.TestCase):

    @classmethod
    @patch("builtins.open")
    def setUpClass(cls, mock_open):
        file_pointer = MagicMock()
        file_pointer.readlines.return_value = ['Monday - Friday\n', '00:01 - 09:00 25 USD\n', '09:01 - 18:00 15 USD\n',
                                               '18:01 - 00:00 20 USD\n', 'Saturday and Sunday\n',
                                               '00:01 - 09:00 30 USD\n', '09:01 - 18:00 20 USD\n',
                                               '18:01 - 00:00 25 USD\n']
        mock_open.return_value = file_pointer
        cls.payment_configuration = ConfigurationFactory.build()
        cls.default_question = Question('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')

    def test_should_have_a_defined_representation_as_string(self):
        answer = Answer(self.payment_configuration, self.default_question)
        str_answer = str(answer)
        self.assertEqual('The amount to pay ASTRID is: 85 USD', str_answer)

    def test_should_be_created_from_a_question_and_a_configuration(self):
        answer = Answer(self.payment_configuration, self.default_question)
        self.assertEqual('ASTRID', answer.name)
        self.assertEqual(85.0, answer.amount)

    def test_should_calculate_the_amount_to_be_paid(self):
        question = Question('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00')
        answer = Answer(self.payment_configuration, question)

        self.assertEqual('RENE', answer.name)
        self.assertEqual(215.0, answer.amount)
