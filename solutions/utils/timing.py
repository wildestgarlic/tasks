import time
from functools import wraps
from typing import Any
from typing import Callable

TEMPLATE = (
    '-----------------------------------'
    '{message}'
    '-----------------------------------'
)


def duration(func: Callable) -> Callable:
    start = time.monotonic()

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        response: Any = func(*args, **kwargs)

        print(TEMPLATE.format(message=f'{(time.monotonic() - start) * 1000}ms'))

        return response

    return wrapper
