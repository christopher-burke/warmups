#!/usr/bin/env python3

"""Free Coffee Cups.

Per 6 coffee cups I buy, I get a 7th cup free. In total, I get 7 cups.
Create a function that takes n cups bought and return the total number of
cups I would get.

Source:
https://edabit.com/challenge/dcdy9QMBbryyWENcm
"""

from math import floor


def total_cups(cups: int, free: int=6) -> int:
    """Total number of coffee cups with a free interval."""
    return floor(cups / free) + cups

def main():
    """Run sample functions. Do not import."""
    assert total_cups(6) == 7
    assert total_cups(3) == 3
    assert total_cups(7) == 8
    assert total_cups(12) == 14
    assert total_cups(213) == 248
    assert total_cups(16) == 18
    print('Passed.')


if __name__ == "__main__":
    main()