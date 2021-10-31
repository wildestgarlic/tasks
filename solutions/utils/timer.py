import time


def duration(start: time.time) -> str:
    return f'{(time.monotonic() - start) * 1000}ms'