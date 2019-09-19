import unittest
from payments_configuration.payments_configuration import PaymentsConfiguration
from payments_configuration.payments_configuration_entry import PaymentsConfigurationEntry
from questions.question_hour_item import QuestionHourItem


class TestPaymentsConfiguration(unittest.TestCase):

    def setUp(self):
        self.weekdays_config = '00:01 - 09:00 25 USD\n09:01 - 18:00 15 USD\n18:01 - 00:00 20 USD'
        self.weekends_config = '00:01 - 09:00 30 USD\n09:01 - 18:00 20 USD\n18:01 - 00:00 25 USD'
        self.payments_config = PaymentsConfiguration(self.weekdays_config, self.weekends_config)

    def test_should_construct_an_object_converting_raw_weekdays_config_into_a_list(self):
        payments_configuration = PaymentsConfiguration(self.weekdays_config, '')
        self.assertEqual(len(payments_configuration.weekdays_config), 3)
        self.assertTrue(isinstance(payments_configuration.weekdays_config[0], PaymentsConfigurationEntry))

    def test_should_construct_an_object_converting_raw_weekends_config_into_a_list(self):
        payments_configuration = PaymentsConfiguration('', self.weekdays_config)
        self.assertEqual(len(payments_configuration.weekend_config), 3)
        self.assertTrue(isinstance(payments_configuration.weekend_config[0], PaymentsConfigurationEntry))

    def test_should_construct_empty_list_for_weekdays_when_no_configuration_is_provided(self):
        payments_configuration = PaymentsConfiguration('', self.weekends_config)
        self.assertEqual(len(payments_configuration.weekdays_config), 0)

    def test_should_construct_empty_list_for_weekends_when_no_configuration_is_provided(self):
        payments_configuration = PaymentsConfiguration(self.weekdays_config, '')
        self.assertEqual(len(payments_configuration.weekend_config), 0)

    def test_get_items_for_should_obtain_the_item_the_question_hour_is_contained_in(self):
        question_hour_item = QuestionHourItem('MO10:00-12:00')
        payment_values = self.payments_config.get_hours_for(question_hour_item)

        self.assertEqual(1, len(payment_values))
        self.assertEqual(15, payment_values[0]['rate'])
        self.assertEqual(2, payment_values[0]['hours'])
