from unittest import TestCase
from mock import patch, MagicMock

from configuration_factory.configuration_factory import ConfigurationFactory
from payments_configuration.payments_configuration import PaymentsConfiguration
from tests.helpers import random_string


class TestConfigurationFactory(TestCase):

    def test_should_build_configuration_using_default_file(self):
        payments_configuration = ConfigurationFactory.build()
        self.assertEqual(len(payments_configuration.weekend_config), 3)

    def test_should_build_configuration_using_default_file_when_provided_file_is_none(self):
        payments_configuration = ConfigurationFactory.build(None)
        self.assertEqual(len(payments_configuration.weekend_config), 3)

    @patch("builtins.open")
    @patch('payments_configuration.payments_configuration.PaymentsConfiguration')
    def test_should_build_configuration_using_given_file_when_is_provided(self, payments_config_class, mock_open):
        expected_file_name = random_string(20)
        file_pointer = MagicMock()
        file_pointer.readlines.return_value = \
            'Monday - Friday\n00:01 - 09:00 25 USD\nSaturday and Sunday\n00:01 - 09:00 30 USD'
        mock_open.return_value = file_pointer

        ConfigurationFactory.build(expected_file_name)

        mock_open.assert_called_with(expected_file_name, 'r')
