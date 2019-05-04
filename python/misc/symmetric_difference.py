#!/usr/bin/env python3

"""Symmetric Difference.

Find the values that do not exist in both sets.
"""


def symmetric_difference_list(M, N):
    """Find the symmetric difference between lists M and N."""
    return sorted([x for x in M if x not in N] +
                  [y for y in N if y not in M]
                  )


def symmetric_difference(M: set, N: set) -> set:
    """Find the symmetric difference between sets M and N."""
    return M ^ N


def main():
    """Run a sample of Symmetric Difference function."""
    M = set([1, 2, 3, 9, 8, ])
    N = set([1, 2, 3, 4, 5, ])

    print(symmetric_difference(M, N))
    print(symmetric_difference_list(list(M), list(N)))


if __name__ == "__main__":
    main()
