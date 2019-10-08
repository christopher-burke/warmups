#!/usr/bin/env python3

"""Minutes to Seconds.

Write a function that takes an integer minutes and converts it to seconds.

Source:
https://edabit.com/challenge/FQyaaJx7orS7tiwz8
"""


def how_many_seconds(mins: int) -> int:
    """Convert minutes to seconds."""
    return mins * 60


def main():
    """Run sample how_many_seconds functions. Do not import."""
    assert how_many_seconds(6) == 360
    assert how_many_seconds(4) == 240
    assert how_many_seconds(8) == 480
    assert how_many_seconds(60) == 3600
    print('Passed.')


if __name__ == "__main__":
    main()
