#!/usr/bin/env python3

"""Hours and Minutes to Seconds.

Write a function that takes two integers hours minutes and
converts them to seconds.

Source:
https://edabit.com/challenge/PjcKZRx8YE5KzRN63
"""


def convert(hours: int, minutes: int) -> int:
    """Convert hours and minutes to total seconds."""
    total_seconds = (minutes * 60) + (hours * 3600)
    return total_seconds


def main():
    """Run sample convert functions. Do not import."""
    assert convert(1, 0) == 3600
    assert convert(1, 3) == 3780
    assert convert(0, 30) == 1800
    print('Passed.')


if __name__ == "__main__":
    main()
