#!/usr/bin/env python3


"""Number letter counts.

If the numbers 1 to 5 are written out in words:

    one, two, three, four, five,

then there are

    3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive
were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example,
342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.


source: https://projecteuler.net/problem=17
"""

from itertools import chain
from math import log10

NUM_TO_WORDS = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
    1000000: 'million',
    1000000000: 'billion',
    1000000000000: 'trillion',
    1000000000000000: 'quadrillion',
    1000000000000000000: 'quintillion',
    1000000000000000000000: 'sextillion',
}


def partition_n(n: str) -> tuple:
    """Return a partition of n.

    The partition is on:
    * High order - digits 100s and greater.
    * Lower order - digits 10s and 1s.

    :return: a tuple of n such that (high order units, low order units).
    """
    return (n[:-2], n[-2:],)


def logic(n, british=True, log10_=False):
    """Logic to convert [n]umber to string.

    :return: List of all numbers to words.
    """
    try:
        if n > 0:
            i, _, d = str(log10(n)).partition('.')
            if log10_ and int(i) > 1 and int(d) == 0:
                return ['one', NUM_TO_WORDS[n]]
        return [NUM_TO_WORDS[n]]
    except KeyError:
        pass  # continue

    output = []
    hundreds_and_more, tens_ones = partition_n(str(n))

    if int(tens_ones) < 20:
        output.extend(logic(int(tens_ones), log10_=False))
    else:
        lower_units = [10**i * int(d)
                       for i, d in enumerate(reversed(tens_ones))]

        for num in lower_units:
            output.extend(logic(num, log10_=False))

    if hundreds_and_more:
        if british and int(tens_ones) > 0:
            output.append(f'and')
        higher_units = [(10**i, int(d))
                        for i, d in enumerate(reversed(hundreds_and_more), 2)]

        for nums in higher_units:
            output.extend(chain(*[logic(num, log10_=False)for num in nums]))

    return list(reversed(output))


def number_to_words(n):
    """Return the string of number to words, no spaces."""
    output = logic(n, log10_=True)
    return ''.join([*output])


if __name__ == "__main__":
    print(len(''.join(list(map(number_to_words, range(1, 1001))))))
