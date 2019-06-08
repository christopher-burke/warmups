#!/usr/bin/env python3

"""Replace Letters With Position In Alphabet.

Create a function that takes a string and replaces each letter with its
appropriate position in the alphabet. "a" is 1, "b" is 2, "c" is 3, etc, etc.

Source:
https://edabit.com/challenge/Bm3JCT6rFrnAhHohy
"""


def alphabet_index(text: str) -> str:
    """Replaces each letter with its appropriate position in the alphabet."""
    return " ".join([str(ord(x.lower())-96)
                     for x in text
                     if ord(x.lower())-96 >= 1 and ord(x.lower())-96 < 27])


def main():
    """Run sample alphabet_index functions. Do not import."""
    print(alphabet_index("Wow, does that work?"))
    print(alphabet_index("The river stole the gods."))
    print(alphabet_index("We have a lot of rain in June."))


if __name__ == "__main__":
    main()
