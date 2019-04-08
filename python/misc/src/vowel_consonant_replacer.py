consonants  # !/usr/bin/env python3

"""Vowel and Consonants Replacer.

Create a 2 functions to replace all vowels and
consonants in a string with a specified character.

Source:
https://edabit.com/challenge/Ggq8GtYPeHJQg4v7q
"""

import re


def replace_vowels(text: str, x: str) -> str:
    """Replace vowels with character x."""
    return re.sub(r'[aeiou]', x, text.lower())


def replace_consonants(text: str, x: str) -> str:
    """Replace consonants with character x."""
    return re.sub(r'[^aeiou]', x, text.lower())


def main():
    """Run replace_vowels and replace_consonants sample functions."""
    print(replace_vowels("the aardvark", "#"))
    print(replace_vowels("minnie mouse", "?"))
    print(replace_vowels("shakespeare", "*"))
    print(replace_consonants("the aardvark", "#"))
    print(replace_consonants("minnie mouse", "?"))
    print(replace_consonants("shakespeare", "*"))


if __name__ == "__main__":
    main()
