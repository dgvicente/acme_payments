from unittest import TestCase
from mock import patch, MagicMock
from payments_configuration.configuration_factory import ConfigurationFactory
from tests.helpers import random_string


class TestConfigurationFactory(TestCase):

    def test_should_build_configuration_using_default_file(self):
        payments_configuration = ConfigurationFactory.build()
        self.assertEqual(len(payments_configuration.weekend_config), 3)

    def test_should_build_configuration_using_default_file_when_provided_file_is_none(self):
        payments_configuration = ConfigurationFactory.build(None)
        self.assertEqual(len(payments_configuration.weekend_config), 3)

    @patch("builtins.open")
    def test_should_build_configuration_using_given_file_when_is_provided(self, mock_open):
        expected_file_name = random_string(20)
        file_pointer = MagicMock()
        file_pointer.readlines.return_value = ['Monday - Friday', '00:01 - 09:00 25 USD', 'Saturday and Sunday',
                                               '00:01 - 09:00 30 USD']
        mock_open.return_value = file_pointer

        ConfigurationFactory.build(expected_file_name)

        mock_open.assert_called_with(expected_file_name, 'r')
