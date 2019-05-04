#!/usr/bin/env python3

"""Days in a Month.
Create a function that takes the month and year
(as integers) and returns the number of days in
that month.

Source:
https://edabit.com/challenge/XZQw3zto7keDWPa5v
"""


from calendar import monthrange


def days_in_month(month: int, year: int) -> int:
    """Return the number of days in a month.

    Uses calendar.monthrange.
    Arguments:
        month {int} -- Integer representation of month.
        year {int} -- Integer representation of year.

    Returns:
        int -- Number of days in the month. -1 if error.

    """
    days = monthrange(month=month, year=year)[-1]
    if days:
        return days
    return -1


def main():
    """Run sample days in month functions."""
    print(days_in_month(year=2018, month=4))
    print(days_in_month(year=2019, month=3))
    print(days_in_month(year=2020, month=2))
    print(days_in_month(year=2021, month=2))


if __name__ == "__main__":
    main()
