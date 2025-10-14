import datetime
import time


def get_current_time():
    return datetime.datetime.now()
# 2025-10-14 10:27:44.92012


def get_current_time_intimestamp(current_time):
    return current_time.timestamp()
# 1760430464.920257
