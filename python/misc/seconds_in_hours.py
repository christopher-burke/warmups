#!/usr/bin/env python3

"""Seconds in Hours.

Write a function that converts hours into seconds.

Source:
https://edabit.com/challenge/nyeNvKWdDFKRAk4Da
"""


def how_many_seconds(hours: int) -> int:
    """Convert hours to seconds."""
    return hours * (60**2)


def main():
    """Run sample how_many_second functions. Do not import."""
    assert how_many_seconds(2) == 7200
    assert how_many_seconds(10) == 36000
    assert how_many_seconds(24) == 86400
    assert how_many_seconds(36) == 129600
    print('Passed.')


if __name__ == "__main__":
    main()
