#!/usr/bin/env python3

"""Maximum Difference.

Given a list of integers, return the difference between the largest and smallest
integers in the list.

Source:
https://edabit.com/challenge/6fx8iNCHETW8KqAui
"""

from typing import List
from operator import sub


def difference(nums: List) -> int:
    """Find the difference between the largest and smallest."""
    return sub(*sorted([func(nums) for func in (min, max,)], reverse=True))


def main():
    """Run sample difference functions. Do not import."""
    assert difference([-9, -8, 6, -9, 15, 6]) == 24
    assert difference([-5, 6, 18, 4, 16, -2]) == 23
    assert difference([-2, 20, -9, -9, -2, -7]) == 29
    assert difference([4, -2, 11, -9, 15, 2]) == 24
    assert difference([15, 10, 3, -6, 6, 19]) == 25
    assert difference([1, 7, 18, -1, -2, 9]) == 20
    assert difference([5, 1, -9, 7, -8, -10]) == 17
    assert difference([-4, 17, -4, 20, -7, 0]) == 27
    assert difference([-2, 11, 11, -3, -3, -3]) == 14
    assert difference([1, 15, 14, 20, 10, 6]) == 19
    assert difference([4, 17, 12, 2, 10, 2]) == 15
    assert difference([-3, 3, 20, 10, 0, 17]) == 23
    assert difference([-3, 6, 20, 9, 6, 7]) == 23
    assert difference([16, 15, 1, 18, -7, -3]) == 25
    assert difference([-7, 4, -4, -3, -8, -9]) == 13
    assert difference([15, 8, 17, 18, 10, 10]) == 10
    assert difference([-3, 20, 16, 8, 18, -10]) == 30
    assert difference([6, 18, 9, 1, 3, 1]) == 17
    assert difference([20, 18, -2, -10, -10, 17]) == 30
    assert difference([18, 20, -7, -4, -2, -8]) == 28
    print('Passed.')


if __name__ == "__main__":
    main()
