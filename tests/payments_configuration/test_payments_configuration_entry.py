import unittest

from payments_configuration.payments_configuration_entry import PaymentsConfigurationEntry
from tests.helpers import random_time, random_number, random_string
from custom_exceptions import ValidationException


class TestPaymentsConfigurationEntry(unittest.TestCase):

    def test_should_construct_an_instance_using_given_initial_time(self):
        initial_time = random_time()
        payments_configuration_entry = PaymentsConfigurationEntry(initial_time, '09:00', 25)
        self.assertEqual(payments_configuration_entry.initial_time, initial_time)

    def test_should_construct_an_instance_using_given_end_time(self):
        end_time = random_time()
        payments_configuration_entry = PaymentsConfigurationEntry('00:01', end_time, 25)
        self.assertEqual(payments_configuration_entry.end_time, end_time)

    def test_should_construct_an_instance_using_given_value(self):
        value = random_number(max_value=1000)
        payments_configuration_entry = PaymentsConfigurationEntry('00:01', '09:00', value)
        self.assertEqual(payments_configuration_entry.value, value)

    def test_should_throw_an_exception_when_initial_time_is_not_valid(self):
        initial_time = random_string(5)
        with self.assertRaises(ValidationException):
            PaymentsConfigurationEntry(initial_time, '23:00', 25)

    def test_should_throw_an_exception_when_end_time_is_not_valid(self):
        end_time = random_string(5)
        with self.assertRaises(ValidationException):
            PaymentsConfigurationEntry('22:00', end_time, 25)
