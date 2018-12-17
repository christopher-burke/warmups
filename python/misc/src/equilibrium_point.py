#!/usr/bin/env python3

"""Equilibrium point

Given an array A of N positive numbers. The task is to find the position where equilibrium first occurs in the array.
Equilibrium position in an array is a position such that the sum of elements below it is equal to the sum of elements after it.

"""


sample = [1, 3, 5, 2, 2]


def equilibrium(A):
    """Find the equilibrium point in the array A."""
    for x in range(len(A)):
        pivot = x
        if sum(A[:pivot]) == sum(A[pivot+1:]):
            return (True, pivot,)
    return (False, -1,)


if __name__ == "__main__":
    print(equilibrium(sample))
