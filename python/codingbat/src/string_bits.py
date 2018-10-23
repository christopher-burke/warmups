#!/usr/bin/env python3

"""String bits.

Given a string, return a new string made of every
other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'

source: https://codingbat.com/prob/p113152
"""


def string_bits(str_):
    """Return a string with every other character.

    :return: Return a string with the odd characters removed.
    """
    return str_[::2]


if __name__ == "__main__":
    assert string_bits('Hello') == 'Hlo'
    assert string_bits('Hi') == 'H'
    assert string_bits('Heeololeo') == 'Hello'
    assert string_bits('HiHiHi') == 'HHH'
    assert string_bits('') == ''
    assert string_bits('Greetings') == 'Getns'
    assert string_bits('Chocoate') == 'Coot'
    assert string_bits('pi') == 'p'
    assert string_bits('Hello Kitten') == 'HloKte'
    assert string_bits('hxaxpxpxy') == 'happy'

    print('Passed.')
