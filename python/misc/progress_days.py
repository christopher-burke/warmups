#!/usr/bin/env python3

"""Progress.

Is Johnny Making Progress?

To train for an upcoming marathon, Johnny goes on one long-distance run
each Saturday. He wants to track how often the number of miles he runs
exceeds the previous Saturday. This is called a progress day.

Create a function that takes in a list of miles run every Saturday
and returns Johnny's total number of progress days.

Source:
https://edabit.com/challenge/2yHQwkecEHZBfHcmN
"""


def progress_days(days: list) -> int:
    """Find the number of progress days."""
    progress = 0
    for index, day in enumerate(days):
        if index+1 < len(days):
            progress += 1 if day < days[index+1] else 0
    return progress


def main():
    """Run sample progress_days. Do not import."""
    assert progress_days([3, 4, 1, 2]) == 2
    assert progress_days([10, 11, 12, 9, 10]) == 3
    assert progress_days([6, 5, 4, 3, 2, 9]) == 1
    assert progress_days([9, 9]) == 0
    assert progress_days([12, 11, 10, 12, 11, 13]) == 2
    print('Passed.')


if __name__ == "__main__":
    main()
