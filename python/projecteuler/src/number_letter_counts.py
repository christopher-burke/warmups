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


def logic(n, british=True, log10_=False):
    """Logic to convert [n]umber to string.

    :return: List of all numbers to words.
    """
    output = []

    if n in range(0, 20):
        return [NUM_TO_WORDS[n]]

    closest_value = min(
        min(NUM_TO_WORDS, key=lambda x: n - x), 10**int(log10(n)))

    if closest_value == n:
        if n > 99:
            output.append('one')
            output.append(f'{NUM_TO_WORDS[n]}')
        elif n < 20:
            output.append(NUM_TO_WORDS[n])
        else:
            raise ValueError(f'{n} caused and issue.')

    elif n > 9 and n < 100:
        digit_value = int(n/10) * 10
        output.append(NUM_TO_WORDS[digit_value])
        output.append(NUM_TO_WORDS[n-digit_value])
    else:
        digit_value = int(n/closest_value)
        output.append(NUM_TO_WORDS[digit_value])
        output.append(NUM_TO_WORDS[closest_value])

        next_iteration = n - (digit_value * closest_value)

        if next_iteration > 0:
            output.append('and')
            output.extend(logic(next_iteration,
                                british=british, log10_=log10_))
    return output


def number_to_words(n):
    """Return the string of number to words, no spaces."""
    output = logic(n, log10_=True)
    return ''.join([*output]).replace(' ', '')


if __name__ == "__main__":
    print(len(''.join([number_to_words(i) for i in range(1, 1001)])))
