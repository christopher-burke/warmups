#!/usr/bin/env python3

"""Area of triangle - Heron's Formula."""


from math import sqrt
from functools import reduce
from operator import mul
from typing import Iterable
from decimal import Decimal


def area_triangle(sides: Iterable) -> Decimal:
    """Find the area of a triangle using Heron's formula."""
    s = sum(sides) / 2.0
    a = reduce(mul,  [s - side for side in sides])
    a = a * s
    return Decimal(round(sqrt(a), 3))


def main():
    """Run sample area_triangle functions. Do not import."""
    assert area_triangle([4, 6, 5]) == 9.922
    assert area_triangle([3, 4, 5]) == 6.0
    assert area_triangle([30, 22, 18]) == 196.66
    print('Passed.')


if __name__ == "__main__":
    main()
