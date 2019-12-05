#!/usr/bin/env python3

"""Switcharoo.

Create a function that takes a string and returns a new string with its
first and last characters swapped, except under three conditions:

If the length of the string is less than two, return "Incompatible.".
If the argument is not a string, return "Incompatible.".
If the first and last characters are the same, return "Two's a pair.".

Source:
https://edabit.com/challenge/tnKZCAkdnZpiuDiWA
"""


def flip_end_chars(txt):
    """Flip the first and last characters if txt is a string."""
    if isinstance(txt, str) and txt and len(txt) > 1:
        first, last = txt[0], txt[-1]
        if first == last:
            return "Two's a pair."
        return "{}{}{}".format(last, txt[1:-1], first)
    return "Incompatible."


def main():
    assert flip_end_chars("Cat, dog, and mouse.") == ".at, dog, and mouseC"
    assert flip_end_chars("Anna, Banana") == "anna, BananA"
    assert flip_end_chars("[]") == "]["
    assert flip_end_chars("") == "Incompatible."
    assert flip_end_chars([1, 2, 3]) == "Incompatible."
    assert flip_end_chars("dfdkf49824fdfdfjhd") == "Two's a pair."
    assert flip_end_chars("#343473847#") == "Two's a pair."
    print('Passed.')


if __name__ == "__main__":
    main()
