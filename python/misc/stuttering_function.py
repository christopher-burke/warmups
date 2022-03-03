#!/usr/bin/env python3

"""Stuttering Function.

https://edabit.com/challenge/gt9LLufDCMHKMioh2
"""

from unittest import TestCase


def stutter(word):
    return f"{word[:2]}... {word[:2]}... {word}?"


def main():
    actual_param, expected_param = [
        "increasing", "adventures", "enticing",
        "unacceptable", "accountable", "incredible", "exquisite",
        "am", "enduring", "outstanding", "astonishing",
        "astounding", "impressive", "revolutionize",
        "recurring", "recollection", "so", "gorgeous", "captivating"
    ], [
        "in... in... increasing?", "ad... ad... adventures?",
        "en... en... enticing?", "un... un... unacceptable?",
        "ac... ac... accountable?", "in... in... incredible?",
        "ex... ex... exquisite?", "am... am... am?",
        "en... en... enduring?", "ou... ou... outstanding?",
        "as... as... astonishing?", "as... as... astounding?",
        "im... im... impressive?", "re... re... revolutionize?",
        "re... re... recurring?", "re... re... recollection?",
        "so... so... so?", "go... go... gorgeous?", "ca... ca... captivating?",
    ]

    for i, w in enumerate(actual_param):
        assert stutter(w) == expected_param[i]
    print('Passed.')


if __name__ == "__main__":
    main()
