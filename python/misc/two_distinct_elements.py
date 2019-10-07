#!/usr/bin/env python3

"""Two Distinct Elements.

In each input list, every number repeats at least once, except for two.

Write a function that returns the two unique numbers.

Source:
https://edabit.com/challenge/yL5WmWTCNwwb4GnR7
"""


def find_unique(lst: list) -> list:
    """Find the unique numbers in a list."""
    return [i for i in lst if lst.count(i) < 2]


def main():
    """Run sample find_unique functions. Do not import."""
    assert find_unique([1, 9, 8, 8, 7, 6, 1, 6]) == [9, 7]
    assert find_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) == [2, 1]
    assert find_unique(
        [9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) == [5, 6]
    assert find_unique([4, 3, 9, 9, 1, 1, 6, 1, 6, 2, 4]) == [3, 2]
    assert find_unique(
        [44, 44, 44, 2, 55, 55, 55, 0, 66, 66, 66]) == [2, 0]
    assert find_unique([-9, -9, -9, 7, -9, -9, 1]) == [7, 1]
    assert find_unique(
        [2, 2, -19, 2, 7, 7, 4, 9, 9, 0, 0, 3, 3, 3]) == [-19, 4]


if __name__ == "__main__":
    main()
