"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math
from typing import List

from solutions.utils.timing import duration

N = 600851475143


@duration
def solution1() -> int:
    return next((
        divider for divider in sieve_of_eratosthenes(math.ceil(math.sqrt(N+1)))[::-1]
        if N % divider == 0
    ))


def sieve_of_eratosthenes(n: int) -> List[int]:
    return [
        number for number in range(2, n+1)
        if not any(
            divider for divider in range(number * 2, math.floor(math.sqrt(n + 1)), number)
            if number % divider == 0
        )
    ]


if __name__ == "__main__":
    print(solution1())
