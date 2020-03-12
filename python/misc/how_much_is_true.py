#!/usr/bin/env python3

"""How much is True.

Create a function which returns the number of True values there are in a list.

Source:
https://edabit.com/challenge/wFpi2zFGxWxfj5mZS
"""

from typing import List

def count_true(lst: List) -> int:
    """Find the total number of True values."""
    return sum([1 for item in lst if item])



def main():
    """Run sample"""
    assert count_true([True, False, False, True, False]) == 2
    assert count_true([False, False, False, False]) == 0
    assert count_true([]) == 0
    assert count_true([False, False, True, True, False, False, False, True, True, True, True, False, True, True, False]) == 8
    assert count_true([True, False, True, True, False, False, False, False, False]) == 3
    assert count_true([False, True, True, False, True, True, False, True, False, True, False, True, False, True, False]) == 8
    assert count_true([True, False, True, True, True, False, True, True, False, False]) == 6
    assert count_true([False, False, False, False, True, False, True, False, True, False, False]) == 3
    assert count_true([True, False, False, False, True, False, False, True, False, False, False]) == 3
    assert count_true([True, True, False, True, False, False, False, False, True, False]) == 4
    assert count_true([True, False, True, True, False, True, True, True, True, False, True, False, True, False]) == 9
    assert count_true([True, False, True, True, True, True, False, True, True, False, True, False, False, False, False]) == 8
    assert count_true([True, True, False, False, False, False, True, False, True, True, False, True]) == 6
    print('Passed.')

if __name__ == "__main__":
    main()