import datetime
import time


def get_current_time():
    """
    Returns the current local date and time.
    
    Returns:
        datetime: The current local date and time.
    """
    return datetime.datetime.now()


def get_current_time_intimestamp():
    """
    Returns the current time as a Unix timestamp.
    
    Returns:
        float: The current time as a Unix timestamp.
    """
    current_time = get_current_time()
    return current_time.timestamp()
