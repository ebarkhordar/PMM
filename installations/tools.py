import random

from random import randrange
from datetime import timedelta, datetime

import pytz

hour = 0


def random_date():
    tz = pytz.timezone('Asia/Tehran')
    start = datetime(2019, 5, 1, 1, 8, 7, 127325, tzinfo=tz)
    end = datetime(2019, 7, 13, 1, 8, 7, 127325, tzinfo=tz)
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def random_cumulative_num():
    global hour
    hour = hour + random.randint(1, 20)
    return hour


print(random_date())

print(random.randint(1, 5))
