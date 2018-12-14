#!/usr/bin/env python3

"""Subarray with given sum.

Given an unsorted array A of size N of non-negative integers,
find a continuous sub-array which adds to a given number.

This code implements the function. Problem listed below:

Input:
    The first line of input contains an integer T
    denoting the number of test cases. Then T test cases follow.
    Each test case consists of two lines.
    The first line of each test case is N and S,
    where N is the size of array and S is the sum.
    The second line of each test case contains N space
    separated integers denoting the array elements.

Output:
    For each testcase, in a new line, print the starting and
    ending positions(0 indexing) of first such occuring
    subarray from the left if sum equals to subarray, else print -1.

Constraints:
    1 <= T <= 100
    1 <= N <= 107
    1 <= Ai <= 1010

Example:
    Input:
        2
        5 12
        1 2 3 7 5
        10 15
        1 2 3 4 5 6 7 8 9 10
    Output:
        1 3
        0 4
"""

from typing import Collection


def subarray_with_given_sum(array: Collection, target: int):
    """Find a subarray with target sum."""
    for i in range(len(array)):
        sum_ = 0
        for j in array[i:]:
            sum_ += j
            if sum_ == target:
                return (i, array.index(j),)
            elif sum_ > target:
                break

    return (-1,)


if __name__ == "__main__":
    print(subarray_with_given_sum(array=[1, 2, 3, 7, 5, ], target=12))
    print(subarray_with_given_sum(array=[2, 3, 7, ], target=12))
    print(subarray_with_given_sum(array=[2, 3, 8, ], target=12))
    print(subarray_with_given_sum(
        array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ], target=15))
