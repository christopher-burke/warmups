#!/usr/bin/env python3

"""Power digit sum


2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?


source: https://projecteuler.net/problem=16
"""

import math


def power_digit_sum(n, exponent):
    """Return the power digit sum.

    Uses math.pow.

    :return: sum of digits after n**2.
    """
    power = str(int(math.pow(n, exponent)))
    return sum([int(i) for i in power])


def main():
    """Run Power digit sum."""
    return power_digit_sum(2, 1000)


if __name__ == "__main__":
    print(main())
