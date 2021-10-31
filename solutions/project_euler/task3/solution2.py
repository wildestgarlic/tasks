"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math
from typing import List

from solutions.utils.timing import duration

N = 600851475143


@duration
def solution2() -> int:
    return next((
        divider for divider in sieve_of_eratosthenes(math.ceil(math.sqrt(N+1)))[::-1]
        if N % divider == 0
    ))


def sieve_of_eratosthenes(n: int) -> List[int]:
    if n < 2:
        return []
    max_ndx = (n - 1) // 2
    sieve = [True] * (max_ndx + 1)
    for ndx in range(int(n ** 0.5) // 2):
        if sieve[ndx]:
            num = ndx * 2 + 3
            sieve[ndx + num:max_ndx:num] = [False] * ((max_ndx - ndx - num - 1) // num + 1)

    return [2] + [ndx * 2 + 3 for ndx in range(max_ndx) if sieve[ndx]]


if __name__ == "__main__":
    print(solution2())
