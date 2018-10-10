#!/usr/bin/env python3

"""Common functions needed for warmups."""


from math import sqrt
from functools import reduce


def prime(n):
    """
    Return True if x is prime, False otherwise.

    :param n: integer n
    :return: True or False
    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if len(factors(n)) == 2:
        return True
    else:
        return False


def factors(n):
    """
    Find the set of factors for n.

    :param n: integer n
    :return: set of factors.
    """
    n_factors = ([i, n//i]
                 for i in range(1, int(sqrt(n) + 1)) if n % i == 0)
    return set(reduce(list.__add__, n_factors))
