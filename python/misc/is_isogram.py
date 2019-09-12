#!/usr/bin/env python3

"""Isogram.

Is the word an Isogram?

An isogram is a word that has no repeating letters, consecutive or
nonconsecutive. Create a function that takes a string and returns either
True or False depending on whether or not it's an "isogram".

Source:
https://edabit.com/challenge/vTGXrd5ntYRk3t6Ma
"""


def is_isogram(word: str) -> bool:
    """Determine if word is an isogram."""
    lowercase_word = word.lower()
    distinct_letters = len(set(lowercase_word))
    total_letters = len(lowercase_word)
    return distinct_letters == total_letters


def main():
    """Run sample is_isogram function. Do not import."""
    assert is_isogram("Algorism") is True
    assert is_isogram("PasSword") is False
    assert is_isogram("Dermatoglyphics") is True
    assert is_isogram("Cat") is True
    assert is_isogram("Filmography") is True
    assert is_isogram("Consecutive") is False
    assert is_isogram("Bankruptcies") is True
    assert is_isogram("Unforgivable") is True
    assert is_isogram("Unpredictably") is True
    assert is_isogram("Moose") is False
    print('Passed.')


if __name__ == "__main__":
    main()
