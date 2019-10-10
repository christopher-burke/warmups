#!/usr/bin/env python3

"""Determine Leap Year.

Create a function that determines if a given year is a leap year.
"""


def is_leap_year(year: int) -> bool:
    """Determine if the year is a leap year."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def main():
    """Run sample is_leap_year functions. Do not import."""
    assert is_leap_year(2003) is False
    assert is_leap_year(2004) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(1800) is False
    assert is_leap_year(1776) is True
    assert is_leap_year(2000) is True
    assert is_leap_year(2020) is True
    assert is_leap_year(2021) is False
    assert is_leap_year(1993) is False
    assert is_leap_year(1996) is True
    print('Passed.')


if __name__ == "__main__":
    main()
