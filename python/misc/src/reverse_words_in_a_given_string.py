#!/usr/bin/env python3

"""Reverse words in a given string.

Given a String of length S, reverse the whole string without reversing the individual words in it. 
Words are separated by dots.

source: https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0
"""


def reverse_words_in_string(text):
    """Reverse the words in a string."""
    reversed_words = reversed([word for word in text.split('.')])
    return '.'.join(reversed_words)


if __name__ == "__main__":
    test_cases = (
        'i.like.this.program.very.much',
        'pqr.mno',
    )

    for test_case in test_cases:
        print(reverse_words_in_string(test_case))
