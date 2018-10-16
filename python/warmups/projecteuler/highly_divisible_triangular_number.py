#!/usr/bin/env python3

"""Highly divisible triangular number.


The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have
over five hundred divisors?

source: https://projecteuler.net/problem=12
"""

try:
    from common import factors
except ModuleNotFoundError:
    import sys
    import os

    file_path = os.path.dirname(__file__)
    warmups_dir = os.path.dirname(file_path)
    sys.path.insert(0, warmups_dir)
    from common import factors

from itertools import count


def triangle_number_generator():
    """Return the next triangle number in sequence.

    This is the Triangular Number Sequence: 1, 3, 6, 10, 15, 21, 28, 36, ...

    :yield: Next triangle number.
    """
    counter = count(1)
    sums = 0 + next(counter)
    while True:
        yield sums
        sums += next(counter)


def main(limit: int):
    """Return the triangle number with factors over the limit.

    :return: Triangle number with over the `limit` divisors.
    """
    for triangle_number in triangle_number_generator():
        if len(factors(triangle_number)) > limit:
            return triangle_number
        else:
            continue


if __name__ == "__main__":
    print(main(limit=500))
