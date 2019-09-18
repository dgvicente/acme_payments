import random
import string
import sys


def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def random_number(min_value=0, max_value=sys.maxint):
    return random.randint(min_value, max_value)


def random_time():
    return '%s:%s' % (random_number(10, 20), random_number(10, 20))