#!/usr/bin/env python3

"""Find the Odd Integer.

Create a function that takes a list and finds the integer 
which appears an odd number of times.

Source:
    https://edabit.com/challenge/9TcXrWEGH3DaCgPBs
"""

from collections import Counter


def find_odd(items: list) -> int:
    """Find the integer which appears an odd number of times.

    This function will find all integers that appear an odd number of times.

    Arguments:
        items {list} -- list of integers.

    Returns:
        int -- Integer which appears an odd number of times

    """
    c = Counter()
    c.update(items)
    return [k for k, v in c.items() if v % 2 > 0]


def main():
    """Run find_odd samples."""
    print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5, ]))
    print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5, ]))
    print(find_odd([10, ]))


if __name__ == "__main__":
    main()
