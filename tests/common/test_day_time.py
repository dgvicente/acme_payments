import unittest

from custom_exceptions import ValidationException
from tests.helpers import random_time, random_string
from common.day_time import DayTime


class TestDayTime(unittest.TestCase):

    def test_should_construct_a_time_object_given_an_string_time(self):
        str_time = random_time()
        obj_time = DayTime(str_time)

        self.assertEqual(int(str_time[0:2]), obj_time.hours)
        self.assertEqual(int(str_time[3:]), obj_time.minutes)

    def test_equality_should_return_true_when_comparing_with_other_equal_time(self):
        str_time = random_time()
        time1 = DayTime(str_time)
        time2 = DayTime(str_time)
        self.assertTrue(time1 == time2)

    def test_comparison_should_return_true_when_first_time_is_less_than_second_time(self):
        minor_time = DayTime('08:00')
        bigger_time = DayTime('08:01')
        self.assertTrue(minor_time < bigger_time)

    def test_less_than_comparison_should_return_false_when_first_time_is_more_than_second_time(self):
        bigger_time = DayTime('08:02')
        minor_time = DayTime('08:01')
        self.assertFalse(bigger_time < minor_time)

    def test_less_than_or_equal_comparison_should_return_true_when_times_are_equal(self):
        str_time = random_time()
        self.assertTrue(DayTime(str_time) <= DayTime(str_time))

    def test_should_raise_a_validation_exception_when_provided_value_is_not_valid(self):
        invalid_value = random_string(5)
        with self.assertRaises(ValidationException):
            DayTime(invalid_value)

    def test_less_than_or_equal_comparison_should_return_true_when_end_time_is_midnight(self):
        initial_time = '18:00'
        midnight = '00:00'
        self.assertTrue(DayTime(initial_time) <= DayTime(midnight))

    def test_add_should_sum_to_times_by_adding_hours_and_minutes(self):
        first_time = DayTime('18:00')
        second_time = DayTime('01:01')
        self.assertEqual(DayTime('19:01'), first_time + second_time)

    def test_subtract_should_return_the_hours_difference_between_hours_with_zero_minutes_by_substracting_hours(self):
        first_time = DayTime('10:00')
        second_time = DayTime('12:00')
        self.assertEqual(2, second_time - first_time)

    def test_subtract_should_take_minutes_into_account_to_calculate_difference_between_times(self):
        first_time = DayTime('10:30')
        second_time = DayTime('12:00')
        self.assertEqual(1.5, second_time - first_time)

    def test_subtract_should_take_midnight_as_hour_number_24(self):
        first_time = DayTime('21:00')
        second_time = DayTime('00:00')
        self.assertEqual(3, second_time - first_time)
