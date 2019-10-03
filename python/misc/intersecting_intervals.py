#!/usr/bin/env python3

"""Intersecting Intervals.

Create a function that takes in a list of intervals and returns how many
intervals overlap with a given point.

An interval overlaps a particular point if the point exists inside the
interval, or on the interval's boundary. For example the point 3 overlaps
with the interval [2, 4] (it is inside) and [2, 3] (it is on the boundary).

Source:
https://edabit.com/challenge/vfTJHRxAGeMxkvxni
"""


def count_overlapping(intervals: list, point: int) -> int:
    """"Find the number of overlapping intervals for a given point."""
    overlap = sum([1 for interval in intervals
                   if interval[0] <= point and point <= interval[1]])
    return overlap


def main():
    """Run sample count_overlapping functions. Do not import."""
    assert count_overlapping([[1, 2], [2, 3], [3, 4]], 5) == 0
    assert count_overlapping([[1, 2], [5, 6], [5, 7]], 5) == 2
    assert count_overlapping([[1, 2], [5, 8], [6, 9]], 7) == 2
    assert count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 5) == 5
    assert count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 6) == 2
    assert count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 2) == 2
    assert count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 1) == 1
    print('Passed.')


if __name__ == "__main__":
    main()
