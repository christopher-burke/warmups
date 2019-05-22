#!/usr/bin/env python3

"""Double Letters.

Create a function that takes a word and returns true if the word
as two consecutive identical letters.

Source:
https://edabit.com/challenge/q3JMk2yqXfNyHWE9c
"""

import re


def double_letters(text: str) -> bool:
    """Determine if text contains two consecutive identical letters.

    Uses `re` module to search for a text.
    """
    if re.search(r"(\w)\1+", text):
        return True
    return False


def main():
    """Run sample double_letters functions. Do not import."""
    print(double_letters("loop"))
    print(double_letters("yummy"))
    print(double_letters("orange"))
    print(double_letters("munchkin"))


if __name__ == "__main__":
    main()
