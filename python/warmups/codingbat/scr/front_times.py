#!/usr/bin/env python3

"""Front Times.

Given a string and a non-negative int n,
we'll say that the front of the string is
the first 3 chars, or whatever is there
if the string is less than length 3.
Return n copies of the front;


front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'

source: https://codingbat.com/prob/p165097
"""


def front_times(str_, n):
    """Return the front three chars of string times n.

    :return: Front three from str_ times three.
    """
    return str_[:3] * n


if __name__ == "__main__":
    assert front_times('Chocolate', 2) == 'ChoCho'
    assert front_times('Chocolate', 3) == 'ChoChoCho'
    assert front_times('Abc', 3) == 'AbcAbcAbc'
    assert front_times('Ab', 4) == 'AbAbAbAb'
    assert front_times('A', 4) == 'AAAA'
    assert front_times('', 4) == ''
    assert front_times('Abc', 0) == ''
    print('Passed.')
