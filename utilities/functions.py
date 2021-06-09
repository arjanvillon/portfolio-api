import time


def generate_timestamp():
    timestamp = round(time.time())
    return str(timestamp)
