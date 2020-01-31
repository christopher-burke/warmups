#!/usr/bin/env python3

"""Get the Sum of All List Elements.

Create a function that takes a list and returns the
sum of all numbers in the list.

Source:
https://edabit.com/challenge/foFKdr68vSENQ9AYB
"""

from typing import List


def get_sum_of_elements(lst: List) -> int:
    """Sum of list."""
    return sum(lst)


def main():
    """Run sample get_sum_of_elements functions. Do not import."""
    assert get_sum_of_elements([2, 7, 4]) == 13
    assert get_sum_of_elements([45, 3, 0]) == 48
    assert get_sum_of_elements([-2, 84, 23]) == 105
    print('Passed.')


if __name__ == "__main__":
    main()
