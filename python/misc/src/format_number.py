#!/usr/bin/env python3

"""Format Number with Comma(s) Separating Thousands.
Create a function that takes a number as
an argument and returns a string formatted
to separate thousands.


Source:
https://edabit.com/challenge/6gtZYiqMWjSgLHAou
"""

from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks.

    grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"

    Source:
    https://docs.python.org/3/library/itertools.html#itertools.islice
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def format_number(number: int):
    """Format the number, separating Thousands."""
    number_string = str(number)
    number_grouped = grouper(reversed(number_string), n=3, fillvalue='')
    number_chunks = [''.join(reversed(num)) for num in number_grouped][::-1]

    return ','.join(number_chunks)


def main():
    """Run sample format_number functions."""
    print(format_number(100000))
    print(format_number(10000010))
    print(format_number(10004000000))
    print(format_number(1000000000000))
    print(format_number(1_000_000_000_000))


if __name__ == "__main__":
    main()
