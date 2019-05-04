#!/usr/bin/env python3

"""Reverse Array In Groups."""

from itertools import islice, chain


def main(A, K):
    """Reverse an array in groups."""
    max_ = len(A)
    start = 0
    result = []
    while max_ > K:
        subgroup = A[start:K]
        subgroup.reverse()
        result.append(subgroup)
        max_ -= K
        start += K
    subgroup = A[start:]
    subgroup.reverse()
    result.append(subgroup)
    return(list(chain(*result)))


if __name__ == "__main__":
    main(A=[1, 2, 3, 4, 5], K=3)
