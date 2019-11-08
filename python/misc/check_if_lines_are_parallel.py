#!/usr/bin/env python3

"""Check If Lines Are Parallel.

Given two lines, determine whether or not they are parallel.

Lines are represented by a list [a, b, c], 
which corresponds to the line ax+by=c.

Source:
https://edabit.com/challenge/8rEEHcmq8rRaTksd7
"""


def lines_are_parallel(line_1, line_2) -> bool:
    """Determine if line_1 and line_2 are parallel.

    line_1 = [a,b,c]
    line_2 = [a,b,c]   
    """
    slope_line_1 = line_1[0] // line_1[1]
    slope_line_2 = line_2[0] // line_2[1]

    if slope_line_1 == slope_line_2:
        return True
    return False


def main():
    """Run sample lines_are_parallel functions. Do not import."""
    assert lines_are_parallel([1, 2, 3], [1, 2, 4]) is True
    assert lines_are_parallel([2, 4, 1], [4, 2, 1]) is False
    assert lines_are_parallel([0, 1, 5], [0, 1, 5]) is True
    assert lines_are_parallel([2, 5, 0], [20, 50, 10]) is True
    assert lines_are_parallel([2, 5, 0], [-200, -500, 10]) is True
    assert lines_are_parallel([400000, 1, 0], [400000, 2, 0]) is False
    assert lines_are_parallel([800, 20, 0], [40, 20, 0]) is False
    assert lines_are_parallel([400000, 1, 0], [800000, 2, 100000]) is True
    assert lines_are_parallel([-5, 7, 100000], [5, -7, -200000]) is True
    print('Passed.')


if __name__ == "__main__":
    main()
