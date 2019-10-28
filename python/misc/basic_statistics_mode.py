#!/usr/bin/env python3

"""Basic Statistics: Mode.

The mode of a group of numbers is the value (or values)
that occur most often (values have to occur more than once).
Given a sorted list of numbers, return a list of all
modes in ascending order.

Source:
https://edabit.com/challenge/uAZcCxNj3TtqvxP34
"""

from collections import Counter


def mode(lst: list) -> list:
    """Find all modes in a list."""
    frequency = Counter(lst)
    max_frequency = max(frequency.values())
    return sorted([k for k, v in frequency.items() if v == max_frequency])


def main():
    """Run sample mode functions. Do not import."""
    assert mode([4, 5, 6, 6, 6, 7, 7, 9, 10]) == [6, ]
    assert mode([4, 5, 5, 6, 7, 8, 8, 9, 9]) == [5, 8, 9, ]
    assert mode([1, 2, 2, 3, 6, 6, 7, 9]) == [2, 6, ]
    print('Passed.')


if __name__ == "__main__":
    main()
