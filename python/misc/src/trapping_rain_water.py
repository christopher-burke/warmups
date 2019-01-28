#!/usr/bin/env python3

"""Trapping Rain Water.

Given an array A of N non-negative integers representing
height of blocks at index i as Ai where the width of 
each block is 1. Compute how much water can be trapped
in between blocks after raining.

source: https://practice.geeksforgeeks.org/problems/trapping-rain-water/0
"""

from itertools import starmap
from operator import sub


def main(A):
    """Find the total amount of rain water that can be trapped.

    Find the height of the smallest side.
    Subtract it from all internal blocks.
    """
    min_height = min([A[0], A[-1]])
    items = [(min_height, x, ) for x in A[1:-1] if x <= min_height]
    rain_water_total = sum(starmap(sub, (items)))
    return rain_water_total


if __name__ == "__main__":
    test_cases = (
        (3, 0, 0, 2, 0, 4,),
        (7, 4, 0, 9,),
        (6, 9, 9,),
    )

    for test_case in test_cases:
        print(main(A=test_case))
