#!/usr/bin/env python3

"""Convert Kilometers to Miles.

In this challenge, you have to implement a function that returns the given
distance kilometers converted into miles. You have to round the result up to
the fifth decimal digit.

Source:
https://edabit.com/challenge/vAk9SBqYmj6hXKfrD
"""

from decimal import Decimal

def km_to_miles(kilometers: int):
    """Convert km to miles."""
    ratio = Decimal('0.621371')
    miles = kilometers * ratio
    return miles

def main():
    """Run sample functions. Do not import."""
    assert km_to_miles(2) == Decimal('1.24274')
    assert km_to_miles(6) == Decimal('3.72823')
    assert km_to_miles(8) == Decimal('4.97097')
    print('Passed'.)

if __name__ == "__main__":
    main()