#!/usr/bin/env python3

"""Multiple of 100.

Create a function that takes an integer and returns
True if it's divisible by 100, otherwise return False.

Source:
https://edabit.com/challenge/NebFhjXTn8NEbhYXY
"""


def divisible(num):
    """Divisible by 100 is True, otherwise return False."""
    return num % 100 == 0


def main():
    """Run sample divisible functions. Do not import."""
    assert divisible(1) is False
    assert divisible(100) is True
    assert divisible(1000) is True
    assert divisible(111000) is True
    assert divisible(-1) is False
    assert divisible(0) is True
    assert divisible(-100) is True
    print('Passed.')


if __name__ == "__main__":
    main()
