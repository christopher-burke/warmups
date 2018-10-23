#!/usr/bin/env python3

"""10001th prime.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?

source: https://projecteuler.net/problem=7
"""

import sys
sys.path.insert(0, '.')
from itertools import count
from simple_warmups.common import prime, factors


def main():
    """
    Find the 10001th prime main method.

    :param n: integer n
    :return: 10001th prime
    """
    primes = {2, }
    for x in count(3, 2):
        if prime(x):
            primes.add(x)
        if len(primes) >= 10001:
            break
    return sorted(primes)[-1]


if __name__ == "__main__":
    print(main())
