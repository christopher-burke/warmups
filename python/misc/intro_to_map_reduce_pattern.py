# !/usr/bin/env python3

"""An Introduction to the Map-Reduce Pattern

You will be implementing a basic case of the map-reduce pattern in programming.
Given a vector stored as a list of integers, find the magnitude of the vector.
Use the standard distance formula for n-dimensional Cartesian coordinates.

Source:
https://edabit.com/challenge/sMtSzctTWs766rRL8
"""

import math


def magnitude(vector: list) -> float:
    """Find the magnitude of the vector.

    The vector is stored as a list of integers.
    """
    return math.sqrt(sum(i**2 for i in vector))


def main():
    """Run sample magnitude functions. Do not import."""
    assert magnitude([3, 4]) == 5
    assert magnitude([0, 0, -10]) == 10
    assert magnitude([]) == 0
    assert magnitude([2, 3, 6, 1, 8]) == 10.677078252031311
    assert magnitude([9, -9, 3]) == 13.076696830622021
    assert magnitude([-24, 94, 4, 0, 10]) == 97.61147473529944
    print('Passed.')


if __name__ == "__main__":
    main()
