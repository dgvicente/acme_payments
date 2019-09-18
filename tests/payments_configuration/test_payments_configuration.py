import unittest
from payments_configuration.payments_configuration import PaymentsConfiguration
from payments_configuration.payments_configuration_entry import PaymentsConfigurationEntry


class TestPaymentsConfiguration(unittest.TestCase):

    def setUp(self):
        self.weekdays_config = '00:01 - 09:00 25 USD\n09:01 - 18:00 15 USD\n18:01 - 00:00 20 USD'
        self.weekends_config = '00:01 - 09:00 30 USD\n09:01 - 18:00 20 USD\n18:01 - 00:00 25 USD'

    def test_should_construct_an_object_converting_raw_weekdays_config_into_a_list(self):
        payments_configuration = PaymentsConfiguration(self.weekdays_config, '')
        self.assertEquals(len(payments_configuration.weekdays_config), 3)
        self.assertTrue(isinstance(payments_configuration.weekdays_config[0], PaymentsConfigurationEntry))

    def test_should_construct_an_object_converting_raw_weekends_config_into_a_list(self):
        payments_configuration = PaymentsConfiguration('', self.weekdays_config)
        self.assertEquals(len(payments_configuration.weekend_config), 3)
        self.assertTrue(isinstance(payments_configuration.weekend_config[0], PaymentsConfigurationEntry))

    def test_should_construct_empty_list_for_weekdays_when_no_configuration_is_provided(self):
        payments_configuration = PaymentsConfiguration('', self.weekends_config)
        self.assertEquals(len(payments_configuration.weekdays_config), 0)

    def test_should_construct_empty_list_for_weekends_when_no_configuration_is_provided(self):
        payments_configuration = PaymentsConfiguration(self.weekdays_config, '')
        self.assertEquals(len(payments_configuration.weekend_config), 0)