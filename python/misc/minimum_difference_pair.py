#!/usr/bin/env python3

"""Minimum Difference Pair.

Given a list of numbers, return the pair of numbers that give the minimum
absolute difference. Return the pair as a list, sorted in ascending order. 
If multiple pairs have the same difference, return the pair with
the smallest sum.

Source:
https://edabit.com/challenge/oLmAshdKHWLP3ck7e
"""

from typing import List
from collections import namedtuple
from itertools import combinations
from operator import sub

pair = namedtuple('Pair', 'pairs difference sum')


def min_difference_pair(nums: List) -> List:
    """Find the pair of numbers that give the minimum absolute difference."""
    nums = sorted(nums)
    num_pairs = combinations(nums, 2)

    pairs = [pair(pairs=i, difference=abs(sub(*i)), sum=sum(i))
             for i in num_pairs]
    min_diff = min([i.difference for i in pairs])
    matches = list(filter(lambda x: x.difference == min_diff, pairs))

    if len(matches) > 1:
        min_sum = min([i.sum for i in matches])
        matches = list(filter(lambda x: x.sum == min_sum, matches))
    return list(matches[0].pairs)


def main():
    assert min_difference_pair(
        [27, 49, 28, 13, -9, -2, 50]) == [27, 28]
    assert min_difference_pair(
        [32, -2, 25, -5, 20, 48, 38, 36, 7, 0]) == [-2, 0]
    assert min_difference_pair(
        [34, 50, 7, 2, -3, 17, -10, 26]) == [-3, 2]
    assert min_difference_pair([-1, 10, -2, 3, -6, -10]) == [-2, -1]
    assert min_difference_pair([15, 2, 17, 19, 5, -4]) == [15, 17]
    assert min_difference_pair(
        [18, -3, -10, 4, 19, -6, 15, 20, 14, 6]) == [14, 15]
    assert min_difference_pair([11, 16, 9, 5, 15, -6, 2]) == [15, 16]
    assert min_difference_pair(
        [-17, 27, -3, 17, -29, 11, 40, 48]) == [11, 17]
    assert min_difference_pair([43, -8, -17, -19, -9]) == [-9, -8]
    assert min_difference_pair([27, 11, 22, 42, 1, 43, 21]) == [21, 22]
    assert min_difference_pair(
        [41, 42, 20, 6, 32, 49, -5, 28, 39, 40, 37]) == [39, 40]
    assert min_difference_pair([22, -3, 4, 1, 46, 21, 0, 29]) == [0, 1]
    assert min_difference_pair(
        [35, 41, 48, 30, 24, 46, -2, -4, 34, 11]) == [34, 35]
    assert min_difference_pair(
        [9, 26, 5, 11, 34, -1, 4, 22, 40, 13, 25]) == [4, 5]
    assert min_difference_pair(
        [28, 19, 29, 35, 24, 3, 23, 30]) == [23, 24]
    assert min_difference_pair([32, 33, 0, 39, 38, 29, 23]) == [32, 33]
    assert min_difference_pair([13, 7, 39, 30, 17, 6, 38, 14]) == [6, 7]
    assert min_difference_pair([2, 26, 1, 30, 29, 11, 12]) == [1, 2]
    assert min_difference_pair(
        [38, 0, 21, -1, 40, 8, 22, 32, 27]) == [-1, 0]
    assert min_difference_pair([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2]
    print('Passed.')


if __name__ == "__main__":
    main()
