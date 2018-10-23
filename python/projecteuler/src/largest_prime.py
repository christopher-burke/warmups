#!/usr/bin/env python3

""" Largest prime factor.

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

source: https://projecteuler.net/problem=3
"""

from math import sqrt
from functools import reduce

try:
    from common import prime
except ModuleNotFoundError:
    import sys
    import os

    file_path = os.path.abspath(__file__)
    warmups_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
    sys.path.insert(0, warmups_dir)
    from common import prime


def prime_factorization(number: int):
    """Return set of prime factors."""
    p = number // 2
    s = set()
    for n in range(1, p+1):
        if number % n == 0 and prime(n):
            s = s | {n}
    return s


if __name__ == "__main__":
    print(13195, sorted(prime_factorization(13195)))
    print(600851475143, sorted(prime_factorization(600851475143)))
