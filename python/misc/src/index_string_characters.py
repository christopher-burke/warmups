#!/usr/bin/env python3

"""Return the Index of All Capital Letters.

Create a function that takes a single string as argument and
returns an ordered list containing the indexes of all
capital letters in the string.

I also included a function for lowercase letters as well.

Source:
https://edabit.com/challenge/rQkriLJBc9CbfRbJb
"""

from string import ascii_uppercase as CAPS

# Defining local CAPS string.
# CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def index_of_caps(text: str) -> list:
    """List of indexes of all capital letters in text."""
    return [index for index, letter in enumerate(text) if letter in CAPS]


index_of_uppercase = index_of_caps


def index_of_lowercase(text: str) -> list:
    """List of indexes of all lowercase letters in text."""
    return [index for index, letter in enumerate(text) if letter not in CAPS]


def main():
    """Run sample functions. Do not import."""
    # Upper case / Capitals
    print(index_of_caps("eDaBiT"))
    print(index_of_caps("eQuINoX"))
    print(index_of_caps("determine"))
    print(index_of_caps("STRIKE"))
    print(index_of_uppercase("sUn"))
    print()
    # Lower Case
    print(index_of_lowercase("eDaBiT"))
    print(index_of_lowercase("eQuINoX"))
    print(index_of_lowercase("determine"))
    print(index_of_lowercase("STRIKE"))
    print(index_of_lowercase("sUn"))


if __name__ == "__main__":
    main()
