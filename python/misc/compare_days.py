#!/usr/bin/env python3

"""Compare Days - Find the number of days between two dates."""

from dateutil.parser import parse


def get_days():
    """Get user input for days to compare."""
    day1 = input('Enter one date (mm/dd/yyyy): ')
    day2 = input('Enter another date (mm/dd/yyyy): ')

    day1 = parse(day1)
    day2 = parse(day2)

    return (day1, day2,)


def compare_days(day1, day2) -> int:
    """Compare the number of days between day1 and day2."""
    days = day1 - day2 if day1 > day2 else day2 - day1
    return days.days


def main():
    """Run compare_days. Main Method, do not import."""
    days = compare_days(*get_days())
    print(f"There are {days} in between.")


if __name__ == "__main__":
    main()
