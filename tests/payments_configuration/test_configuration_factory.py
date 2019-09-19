from unittest import TestCase
from mock import patch, MagicMock
from payments_configuration.configuration_factory import ConfigurationFactory
from tests.helpers import random_string


@patch("builtins.open")
class TestConfigurationFactory(TestCase):

    def setUp(self):
        self.file_pointer = MagicMock()
        self.file_pointer.readlines.return_value = ['Monday - Friday', '00:01 - 09:00 25 USD', 'Saturday and Sunday',
                                                    '00:01 - 09:00 30 USD']

    def test_should_build_configuration_using_default_file(self, mock_open):
        mock_open.return_value = self.file_pointer
        payments_configuration = ConfigurationFactory.build()
        self.assertEqual(1, len(payments_configuration.weekend_config))

    def test_should_build_configuration_using_default_file_when_provided_file_is_none(self, mock_open):
        mock_open.return_value = self.file_pointer
        payments_configuration = ConfigurationFactory.build(None)
        self.assertEqual(1, len(payments_configuration.weekend_config))

    def test_should_build_configuration_using_given_file_when_is_provided(self, mock_open):
        expected_file_name = random_string(20)
        mock_open.return_value = self.file_pointer

        ConfigurationFactory.build(expected_file_name)

        mock_open.assert_called_with(expected_file_name, 'r')

    def test_should_use_given_regex_when_provided(self, mock_open):
        mock_open.return_value = self.file_pointer
        self.file_pointer.readlines.return_value = ['Lunes - Viernes', '00:01 - 09:00 25 USD', 'Sabado y Domingo',
                                                    '00:01 - 09:00 30 USD']
        payments_configuration = ConfigurationFactory.build(
            pattern='Lunes.*Viernes\n*(?P<weekdays>.*\s*)Sabado.*Domingo\n*(?P<weekends>.*\s*)')
        self.assertEqual(1, len(payments_configuration.weekend_config))
