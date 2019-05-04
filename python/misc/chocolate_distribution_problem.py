#!/usr/bin/env python3

"""Chocolate Distribution Problem.

source:https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem/0
"""


def chunks(A, N):
    """Yield sublist of A of length N."""
    for i in range(0, len(A)):
        r = A[i:i+N]
        if len(r) == N:
            yield r


def main(A, N):
    """Chocolate Distribution Problem."""
    A = sorted(A)
    min_ = None
    for x in chunks(A, N):
        diff = x[-1] - x[0]
        if min_ is None or diff <= min_:
            min_ = diff

    return min_


if __name__ == "__main__":
    test_cases = [
        ([3, 4, 1, 9, 56, 7, 9, 12, ], 5),
        ([7, 3, 2, 4, 9, 12, 56, ], 3),
    ]

    for A, N in test_cases:
        print(main(A, N))
