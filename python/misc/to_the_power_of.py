#!/usr/bin/env python3

"""To the Power of.

Create a function that takes a base number and an exponent number and
returns the calculation.

Source:
https://edabit.com/challenge/xWSjvoH7mEkSnqS7H
"""


def calculate_exponent(number: int, exponent: int) -> int:
    """Calculate the number raised to the power of exponent."""
    return number ** exponent


def main():
    """Run sample calculate_exponent functions. Do not import."""
    calculate_exponent(5, 5) == 3125
    calculate_exponent(3, 3) == 27
    calculate_exponent(10, 10) == 10000000000
    print('Passed.')


if __name__ == "__main__":
    main()
