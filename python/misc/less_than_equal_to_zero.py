#!/usr/bin/env python3

"""Less than or equal to zero.

Is the Number Less than or Equal to Zero?

Create a function that takes a number as its only argument and returns
True if it's less than or equal to zero, otherwise return False.

Source:
https://edabit.com/challenge/Rx2pkSA9dCmtwS8xt
"""


def less_than_or_equal_to_zero(number: int) -> bool:
    """Determine number less than or equal to zero."""
    return number <= 0


def main():
    """Run sample less_than_or_equal_to_zero functions. Do not import."""
    assert less_than_or_equal_to_zero(5) is False
    assert less_than_or_equal_to_zero(0) is True
    assert less_than_or_equal_to_zero(-5) is True
    print('Passed.')


if __name__ == "__main__":
    main()
