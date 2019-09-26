#!/usr/bin/env python3

"""Numbers in Strings.

Create a function that takes a list of strings and returns
a list with only the strings that have numbers in them.
If there are no strings containing numbers, return an empty list.

Source:
https://edabit.com/challenge/XYYdtkhGPXXJ3QQNB
"""


import re


def num_in_str(lst: list) -> list:
    """Create a list of strings that have numbers in it."""
    return [i for i in lst if re.search(r"\d", i)]


def main():
    """Run sample num_in_str functions. Do not import."""
    assert num_in_str(['abc', 'abc10']) == ['abc10']
    assert num_in_str(
        ['abc', 'ab10c',  'a10bc', 'bcd']) == ['ab10c', 'a10bc']
    assert num_in_str(['1', 'a', ' ', 'b']) == ['1']
    assert num_in_str(['rct', 'ABC', 'Test', 'xYz']) == []
    assert num_in_str(['this IS', '10xYZ', 'xy2K77', 'Z1K2W0', 'xYz']) == [
        '10xYZ', 'xy2K77', 'Z1K2W0']
    assert num_in_str(['-/>', '10bc', 'abc ']) == ['10bc']
    print('Passed.')


if __name__ == "__main__":
    main()
