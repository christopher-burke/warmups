#!/usr/bin/env python3

"""Valid Zip Code.

Zip codes consist of 5 consecutive digits.
Given a string, write a function to determine
whether the input is a valid zip code.

Source:
https://edabit.com/challenge/Jv6KqxKp2F6p7YLhf
"""

import re


def is_valid(zip_code: str) -> bool:
    """Determine valid zip code using re.match."""
    return bool(re.match(r"\d\d\d\d\d", zip_code))


def main():
    """Run is_valid function with sample data."""
    print(is_valid("59001"))  # ➞ True
    print(is_valid("853a7"))  # ➞ False
    print(is_valid("732 32"))  # ➞ False


if __name__ == "__main__":
    main()
