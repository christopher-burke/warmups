#!/usr/bin/env python3

""" To the Power of _. Calculate Exponent.

Create a function that takes a base number and
an exponent number and returns the calculation.

Source:
https://edabit.com/challenge/xWSjvoH7mEkSnqS7H
"""


def calculate_exponent(base: int, exponent: int) -> int:
    """Return the base^exponent (base ** exponent)."""
    return base**exponent


def main():
    """Run sample calculate_exponent functions. Do not import."""
    print(calculate_exponent(5, 5))
    print(calculate_exponent(10, 10))
    print(calculate_exponent(3, 3))


if __name__ == "__main__":
    main()
