#!/usr/bin/env python3

"""Check String for Spaces.

Create a function that returns True if a string contains any spaces.

An empty string does not contain any spaces.
Try doing this without RegEx.

Source:
https://edabit.com/challenge/rR2qf7ELnXoXESiz2
"""


def has_spaces(txt:str) -> bool:
    """Determine if txt has spaces."""
    return len(txt.split(" ")) > 1


def main():
    """Run sample has_spaces functions. Do not import."""
    assert has_spaces("Foo") == False
    assert has_spaces("Foo bar") == True
    assert has_spaces("Foo ") == True
    assert has_spaces(" Foo") == True
    assert has_spaces(" ") == True
    assert has_spaces("") == False
    assert has_spaces(",./;'[]-=") == False
    print('Passed.')

if __name__ == "__main__":
    main()