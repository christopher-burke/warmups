#!/usr/bin/env python3

"""Make abba.

Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'

source: https://codingbat.com/prob/p182144
"""


def make_abba(a, b):
    """Return the result of putting them together in the order abba.

    Given two strings, a and b, return the
    result of putting them together in the order abba.

    e.g. "Hi" and "Bye" returns "HiByeByeHi".
    """
    return f"{a}{b*2}{a}"


def main():
    """Test the make_abba function."""
    assert make_abba('Yo', 'Alice') == 'YoAliceAliceYo'
    assert make_abba('Hi', 'Bye') == 'HiByeByeHi'
    assert make_abba('What', 'Up') == 'WhatUpUpWhat'
    assert make_abba('aaa', 'bbb') == 'aaabbbbbbaaa'
    assert make_abba('x', 'y') == 'xyyx'
    assert make_abba('x', '') == 'xx'
    assert make_abba('', 'y') == 'yy'
    assert make_abba('Bo', 'Ya') == 'BoYaYaBo'
    assert make_abba('Ya', 'Ya') == 'YaYaYaYa'
    print('Passed.')


if __name__ == "__main__":
    main()
