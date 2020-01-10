#!/usr/bin/env python3

"""Difference of Max and Min Numbers in List.

Create a function that takes a list and returns the
difference between the biggest and smallest numbers.

Source:
https://edabit.com/challenge/XsJLwhAddzbxdQqr4
"""


def difference_max_min(lst) -> int:
    """Return the difference between max and min in lst."""
    return max(lst) - min(lst)


def main():
    """Run sample difference_max_min functions. Do not import."""
    assert difference_max_min([10, 4, 1, 2, 8, 91]) == 90
    assert difference_max_min([-70, 43, 34, 54, 22]) == 124
    print('Passed.')


if __name__ == "__main__":
    main()
