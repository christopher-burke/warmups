#!/usr/bin/env python3

"""Positive Count / Negative Sum.

Create a function that takes a list of positive and negative numbers.
Return a list where the first element is the count of positive numbers
and the second element is the sum of negative numbers.

Source:
https://edabit.com/challenge/RTZRnXCJkfALTTdqt
"""

from typing import List


def sum_neg(numbers: List) -> List:
    """Return a list of: Count of Positive and Sum of Negative numbers."""
    if numbers:
        # Solve the positive count using list() and filter() builtins.
        positive_count = len(list(filter(lambda x: x >= 0, numbers)))
        # Solve the negative sum using list comprehension.
        negative_sum = sum([num for num in numbers if num < 0])
        return [positive_count, negative_sum]

    return []


def main():
    """Run the sample sum_neg functions. Do not import."""
    print(sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
    print(sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34]))
    print(sum_neg([91, -4, 80, -73, -28]))
    print(sum_neg([]))


if __name__ == "__main__":
    main()
