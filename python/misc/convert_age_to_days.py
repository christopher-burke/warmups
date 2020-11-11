#!/usr/bin/env python3

"""Convert Age to Days.

Create a function that takes the age and return the age in days.

Source:
https://edabit.com/challenge/bL7hSc6Zh4zZJzGmw
"""


def calculate_age(years: int):
    """Convert years to days."""
    return years * 365


def main():
    assert calculate_age(years=65) == 23725
    assert calculate_age(years=0) == 0
    assert calculate_age(years=20) == 7300
    assert calculate_age(years=10) == 3650
    assert calculate_age(73) == 26645
    print('Passed.')


if __name__ == "__main__":
    main()
