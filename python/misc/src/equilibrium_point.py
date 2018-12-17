#!/usr/bin/env python3

"""Equilibrium point

Given an array A of N positive numbers. The task is to find the position where equilibrium first occurs in the array.
Equilibrium position in an array is a position such that the sum of elements below it is equal to the sum of elements after it.

"""


sample = [1, 3, 5, 2, 2]


def equilibrium(A):
    """Find the equilibrium point in the array A."""

    total_sum = sum(A)
    left_sum = 0

    for i, num in enumerate(A):
        total_sum -= num

        if left_sum == total_sum:
            return (True, i,)
        left_sum += num

    return (False, -1,)


if __name__ == "__main__":
    print(equilibrium(sample))
