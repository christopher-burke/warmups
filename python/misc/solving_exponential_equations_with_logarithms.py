#!/usr/bin/env python3

"""Solving Exponential Equations With Logarithms.

Create a function that takes a number a and finds the missing exponent
x so that a when raised to the power of x is equal to b.

Source:
https://edabit.com/challenge/MhQbon8XzsG3wJHdP
"""

from math import log


def solve_for_exp(a, b):
    """Find the missing exponent.

    a=base
    b=result"""
    return int(round(log(b, a)))


def main():
    assert solve_for_exp(4, 1024) == 5
    assert solve_for_exp(2, 1024) == 10
    assert solve_for_exp(9, 3486784401) == 10
    assert solve_for_exp(4, 4294967296) == 16
    assert solve_for_exp(8, 134217728) == 9
    assert solve_for_exp(19, 47045881) == 6
    assert solve_for_exp(10, 100000000) == 8
    print('Passed.')


if __name__ == "__main__":
    main()
