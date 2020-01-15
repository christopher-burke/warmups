#!/usr/bin/env python3

"""Apocalyptic Numbers.

In this challenge, you have to establish if a number is apocalyptic.
A positive integer n greater than 0 is apocalyptic when 2 elevated to n contains one or more occurrences of 666 into it.

Given an integer n, implement a function that returns:
    * "Safe" if n is not apocalyptic.
    * "Single" if into 2^n there's a single occurence of 666.
    * "Double" if into 2^n there are two occurences of 666.
    * "Triple" if into 2^n there are three occurences of 666.

Source:
https://edabit.com/challenge/gHrMmA7emP6CFAMnb
"""


import re


RESULT = {
    '1': 'Single',
    '2': 'Double',
    '3': 'Triple',
}


def is_apocalyptic(number: int) -> str:
    """Determine if number is apocalyptic."""
    if number > 0 and number <= 1000:
        test_if_apocalyptic = str(2**number)
    else:
        raise ValueError(
            "Any given n will be a positive integer in the range of 1 to 1000.")

    result = str(len(re.findall(r'666', test_if_apocalyptic)))

    return RESULT.get(result, 'Safe')


def main():
    """Run sample is_apocalyptic functions. Do not import."""
    assert is_apocalyptic(66) == "Safe"
    assert is_apocalyptic(157) == "Single"
    assert is_apocalyptic(220) == "Double"
    assert is_apocalyptic(931) == "Triple"
    assert is_apocalyptic(166) == "Safe"
    assert is_apocalyptic(529) == "Double"
    assert is_apocalyptic(443) == "Single"
    assert is_apocalyptic(166) == "Safe"
    assert is_apocalyptic(703) == "Safe"
    assert is_apocalyptic(528) == "Single"
    assert is_apocalyptic(648) == "Double"
    print('Passed.')


if __name__ == "__main__":
    main()
