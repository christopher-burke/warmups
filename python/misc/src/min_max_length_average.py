#!/usr/bin/env python3

"""Find the Minimum, Maximum, Length and Average Values.

Create a function that takes a list of numbers
and returns the following statistics:

* Minimum Value
* Maximum Value
* Sequence Length
* Average Value

Source:
    https://edabit.com/challenge/pnkw3XYjG8bbB6Fva
"""

from collections import namedtuple
from statistics import mean

results = namedtuple("MinMaxLengthAverage", "min max length average")


def minMaxLengthAverage(a: list) -> results:
    """Find the min max length and average of a list.

    Arguments:
        a {list} -- List of numbers

    Returns:
        namedtuple {namedtuple} --  Min, Max, Length, and Average.

    """
    min_ = min(a)
    max_ = max(a)
    len_ = len(a)
    average = mean(a)
    return results(min=min_, max=max_, length=len_, average=average)


def main():
    """Run sample minMaxLengthAverage functions."""
    print(minMaxLengthAverage([6, 9, 15, -2, 92, 11]))
    print(minMaxLengthAverage([30, 43, 20, 92, 3, 74]))
    print(minMaxLengthAverage([4.54, 8.32, 5.20]))


if __name__ == "__main__":
    main()
