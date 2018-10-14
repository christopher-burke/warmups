#!/usr/bin/env python3

"""Summation of primes.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

source: https://projecteuler.net/problem=10
"""

from itertools import count, islice
from math import sqrt
from functools import reduce


def factors(n):
    """Find all factors of a number n.

    https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    """
    n_factors = ([i, n//i] for i in range(1, int(sqrt(n) + 1)) if n % i == 0)
    return set(reduce(list.__add__, n_factors))


def prime(n: int) -> bool:
    """
    Return True if x is prime, False otherwise.

    :return: True if prime, False if not prime.
    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if len(factors(n)) == 2:
        return True
    else:
        return False


def primes(limit: int) -> tuple:
    """
    Find all prime numbers below limit.

    :return: Tuple of prime numbers below limit.
    """
    counter = islice(count(2), limit)
    return tuple(c for c in counter if prime(c))


def main(limit: int) -> int:
    """
    Return the sum of primes below n.

    :return: Sum of primes below limit.
    """
    primes_lt_limit = primes(limit)
    return sum(primes_lt_limit)


if __name__ == "__main__":
    print(main(limit=2000000))
