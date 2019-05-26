#!/usr/bin/env python3

"""Day of the week.

Find the day of the week given a date.
"""

from datetime import datetime
import calendar


def day_of_week(date: datetime) -> str:
    """Get the day of the week."""
    weekday = date.weekday()
    return calendar.day_name[weekday]


def main():
    """Main method, run sample day_of_week functions. Do not import"""
    print(day_of_week(datetime.now()))
    print(day_of_week(datetime(2019, 7, 4)))
    print(day_of_week(datetime(2013, 12, 25)))
    print(day_of_week(datetime(2000, 1, 1)))


if __name__ == "__main__":
    main()
