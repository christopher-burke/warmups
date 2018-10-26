#!/usr/bin/env python3

"""Number letter counts


If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


source: https://projecteuler.net/problem=17
"""

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


def logic(n, british=True):
    # TODO: It works, but it needs refactoring.
    try:
        return NUM_TO_WORDS[n]
    except KeyError:
        pass

    number_string = str(n)

    output = []
    if len(number_string) > 1:
        ten_ones_ = number_string[-2:]
        number_string = reversed(number_string[:-2])

        if int(ten_ones_) > 0 and int(ten_ones_) < 20:
            output.append(NUM_TO_WORDS[int(ten_ones_)])

        else:
            if int(ten_ones_[0]) > 0:
                output.append(NUM_TO_WORDS[int(ten_ones_[0]) * 10])
            if int(ten_ones_[1]) > 0:
                output.append(NUM_TO_WORDS[int(ten_ones_[1])])

    for place, digit in enumerate(number_string, 2):
        multiplier = 10**place
        digit = int(digit)
        if place is 2 and british:
            output.append('AND')
        if digit > 0:
            output.append(NUM_TO_WORDS[multiplier])
            output.append(NUM_TO_WORDS[digit])
    return reversed(output)


def number_to_words(n):
    output = logic(n)
    return ''.join(output)


if __name__ == "__main__":
    print(len(''.join(list(map(number_to_words, range(1, 1001))))))
