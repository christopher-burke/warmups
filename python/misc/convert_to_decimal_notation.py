#!/usr/bin/env python3

"""Convert to Decimal Notation.

Create a function to convert an array of percentages to
their decimal equivalents.

Source:
https://edabit.com/challenge/4tLabih2cr5Haw7xo
"""

from decimal import Decimal


def convert_to_decimal(iterable) -> list:
    """Return a list of percentages to their decimal equivalents."""
    return [Decimal(x.partition('%')[0]) / Decimal(100)
            for x in iterable]


def main():
    """Run sample convert_to_decimal functions."""
    print(convert_to_decimal(["1%", "2%", "3%"]))
    print(convert_to_decimal(["45%", "32%", "97%", "33%"]))
    print(convert_to_decimal(["33%", "98.1%", "56.44%", "100%"]))


if __name__ == "__main__":
    main()
