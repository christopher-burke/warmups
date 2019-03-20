#!/usr/bin/env python3

"""Number to month."""

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


def month_name(month: int) -> str:
    """Return the month name from the month number.

    Arguments:
        month {int} -- Month number.

    Raises:
        TypeError -- month type integer.

    Returns:
        str -- String name of the month.

    """

    if type(month) is not int:
        raise TypeError("month is not Integer.")
    return months.get(month)


def main():
    """Run sample month_name functions."""
    print(month_name(3))
    print(month_name(12))
    print(month_name(6))
    print(month_name(True))


if __name__ == "__main__":
    main()
