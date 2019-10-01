#!/usr/bin/env python3

"""Find the Odd Integer.

Create a function that takes a list and finds the integer which appears
an odd number of times.

Source
https://edabit.com/challenge/9TcXrWEGH3DaCgPBs
"""

from collections import Counter


def find_odd(lst: list) -> int:
    """Find the integer that appears an odd number of times."""
    return [k for k, v in Counter(lst).items() if v % 2 != 0][-1]


def main():
    """Run sample find_odd functions."""
    assert find_odd([20, 1, -1, 2, -2, 3, 3, 5, 5,
                     1, 2, 4, 20, 4, -1, -2, 5]) == 5
    assert find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) == -1
    assert find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) == 5
    assert find_odd([10]) == 10
    assert find_odd([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]) == 10
    assert find_odd([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]) == 1
    print('Passed.')


if __name__ == "__main__":
    main()
