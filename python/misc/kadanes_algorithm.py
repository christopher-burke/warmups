#!/usr/bin/env python3

"""Kadane's Algorithm

source : https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

Constraints:
    1 ≤ T ≤ 200
    1 ≤ N ≤ 1000
    -100 ≤ A[i] <= 100

Example:
Input
    2
    3
    1 2 3
    4
    -1 -2 -3 -4
Output
    6
    -1
"""

from typing import Iterable


def max_subarray_sum(nums: Iterable, size: int) -> int:
    """Return the contiguous sub-array with maximum sum."""
    max_sum_ = nums[0]
    current_max_sum_ = nums[0]
    for i in range(1, size):
        current_max_sum_ = max(nums[i], current_max_sum_ + nums[i])
        max_sum_ = max(max_sum_, current_max_sum_)
    return max_sum_


if __name__ == "__main__":
    tests = [
        ([1, 2, 3], 3, 6),
        ([1, -3, 2, 1, -1], 5, 3),
        ([-1, -2, -3, -4], 4, -1),
        ([-2, -3, 4, -1, -2, 1, 5, -3], 8, 7),
        ([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7], 13, -3)
    ]

    for test in tests:
        nums = test[0]
        size = test[1]
        result = max_subarray_sum(nums=nums, size=size)
        print(result)

        assert result == test[-1], (result, test[-1])
