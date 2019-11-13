#!/usr/bin/env python3

"""Concatenate Variable Number of Input Lists.

Create a function that concatenates n input lists, where n is variable.

Source:
https://edabit.com/challenge/woA74HtrheoQva87R
"""

from itertools import chain


def concat(*args):
    """Concatenate n input lists."""
    return list(chain(*args))


def main():
    """Run sample concat functions. Do not import."""
    assert concat([1, 2, 3], [4, 5], [6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert concat([1], [2], [3], [4], [5], [6], [7]) == [1, 2, 3, 4, 5, 6, 7]
    assert concat([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert concat([4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4]
    assert concat(['a'], ['b', 'c']) == ['a', 'b', 'c']
    print('Passed.')


if __name__ == "__main__":
    main()
