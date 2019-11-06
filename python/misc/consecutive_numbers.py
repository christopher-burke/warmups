#!/usr/bin/env python3

"""Consecutive Numbers.

Create a function that determines whether elements in an array can be re-arranged to form a consecutive list of
numbers where each number appears exactly once.

Source:
https://edabit.com/challenge/oKjqFFzaybbs8csiE
"""


from typing import List


def arithmetic_series(a, d, n):
    """Find the sum of arithmetic series.

    a = first term
    d = Common Difference
    n = number of terms
    """
    sum_ = (n/2) * (2 * a + (n-1) * d)
    return sum_


def cons(array: List) -> bool:
    """Determine if list can form a consecutive list of numbers."""
    return sum(array) == \
        int(arithmetic_series(min(array), 1, len(array)))


def main():
    """Run sample cons functions. Do not import."""
    assert cons([5, 1, 4, 3, 2])is True
    assert cons([55, 59, 58, 56, 57])is True
    assert cons([-3, -2, -1, 1, 0])is True
    assert cons([5, 1, 4, 3, 2, 8])is False
    assert cons([5, 6, 7, 8, 9, 9])is False
    assert cons([5, 3])is False
    print('Passed.')


if __name__ == "__main__":
    main()
