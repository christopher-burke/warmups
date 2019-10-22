#!/usr/bin/env python3

"""Number Symmetrical.

Is the Number Symmetrical?

Create a function that takes a number as an argument and returns True or False
depending on whether the number is symmetrical or not.
A number is symmetrical when it is the same as its reverse.

Source:
https://edabit.com/challenge/zqMREZ2MQd9M5jNfM
"""


def is_symmetrical(num: int) -> bool:
    """Determine if num is symmetrical."""
    num_str = str(num)
    return num_str[::-1] == num_str


def main():
    """Run sample is_symmetrical functions."""
    assert is_symmetrical(23) is False
    assert is_symmetrical(9562) is False
    assert is_symmetrical(10019) is False
    assert is_symmetrical(1) is True
    assert is_symmetrical(3223) is True
    assert is_symmetrical(95559) is True
    assert is_symmetrical(66566) is True
    print('Passed.')


if __name__ == "__main__":
    main()
