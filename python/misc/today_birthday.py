#!/usr/bin/env python3

"""Today Birthday.

Is today a birthday?

"""


from datetime import datetime
from dateutil.parser import parse
from operator import attrgetter


def day_month(date: datetime) -> tuple:
    """Return tuple of (day, month,) from given date."""
    return attrgetter('day', 'month')(date)


def input_birthdate() -> datetime:
    """Get birthdate from user."""
    birthdate = input('The birthdate (mm/dd/yyyy): ')
    birthdate = parse(birthdate)
    return birthdate


def calculate_age(year1: int, year2: int) -> int:
    """Find the difference between years (age)."""
    age = abs(year2 - year1)
    return age


def result(birthdate: datetime.date) -> str:
    """Process the birthdate and return the result."""
    today = datetime.now().date()
    if birthdate == today:
        return "Date entered was today."
    if (day_month(birthdate)) == (day_month(today)):
        age = calculate_age(today.year, birthdate.year)
        return f"Happy Birthday! " + \
            f"Age now is now {age} year{'s' if age > 1 else ''} old."
    return f"The birthdate {birthdate} is not today."


def run() -> str:
    """Run function. Do not import."""
    birthdate = input_birthdate().date()
    return result(birthdate)


def main():
    """Run the run function. Do not import."""
    print(run())


if __name__ == "__main__":
    main()
