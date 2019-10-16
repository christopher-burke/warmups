#!/usr/bin/env python3

"""Return the First Element in a List.

Create a function that takes a list and returns the first element.

Source:
https://edabit.com/challenge/hEQ3rBrKrztQK8qAd
"""


def get_first_value(num_list: list):
    """Find the first value in iterable."""
    return num_list[0]


def main():
    """Run sample get_first_value functions. Do not import."""
    assert get_first_value([1, 2, 3]) == 1
    assert get_first_value([80, 5, 100]) == 80
    assert get_first_value([-500, 0, 50]) == -500
    assert get_first_value([5, 2, 3]) == 5
    assert get_first_value([75675, 5, 100]) == 75675
    assert get_first_value([-52320, 0, 50]) == -52320
    print('Passed.')


if __name__ == "__main__":
    main()
