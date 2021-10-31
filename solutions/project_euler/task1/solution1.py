"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time

from utils.timer import duration

N = 1000


def solution1() -> int:
    return sum((number for number in range(N) if number % 3 == 0 or number % 5 == 0))


if __name__ == "__main__":
    start = time.monotonic()
    print(solution1(), duration(start))
