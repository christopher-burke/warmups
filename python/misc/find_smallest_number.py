#!/usr/bin/env python3

"""Find the Smallest Number in a List.

Create a function that takes a list of numbers and returns the
smallest number in the list.

Source:
https://edabit.com/challenge/ecSZ5kDBwCD3ctjE6
"""

from typing import List


def find_smallest_num(lst: List):
    """Find the smallest number in lists."""
    return min(lst)


def main():
    """Run sample find_smallest_num functions. Do not import."""
    assert find_smallest_num([-76, 1.345, 1, 0]) == -76
    assert find_smallest_num([34, 15, 88, 2]) == 2
    assert find_smallest_num([34, -345, -1, 100]) == -345
    assert find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]) == -0.9999
    assert find_smallest_num([7, 7, 7]) == 7
    assert find_smallest_num([4, 6, 1, 3, 4, 5, 5, 1]) == 1
    assert find_smallest_num([-4, -6, -8, -1]) == -8
    assert find_smallest_num([54, 76, 23, 54]) == 23
    assert find_smallest_num([100]) == 100
    assert find_smallest_num([0, 1, 2, 3, 4, 5]) == 0
    print('Passed.')


if __name__ == "__main__":
    main()
