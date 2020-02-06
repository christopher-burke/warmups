#!/usr/bin/env python3

"""Concatenating Two Integer Lists.

Create a function to concatenate two integer lists.

Source:
https://edabit.com/challenge/cCWMeiJCP9Ef8XMq8
"""

from typing import List


def concat(lst1: List, lst2: List) -> List:
    """Concatenate two integer lists."""
    return lst1 + lst2


def main():
    """Run sample concat functions. Do not import."""
    assert concat([1, 3, 5], [2, 6, 8]) == [1, 3, 5, 2, 6, 8]
    assert concat([7, 8], [10, 9, 1, 1, 2]) == [7, 8, 10, 9, 1, 1, 2]
    assert concat([4, 5, 1], [3, 3, 3, 3, 3]) == [4, 5, 1, 3, 3, 3, 3, 3]
    print("Passed.")


if __name__ == "__main__":
    main()
