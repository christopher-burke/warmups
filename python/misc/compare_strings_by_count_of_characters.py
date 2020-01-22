#!/usr/bin/env python3

"""Compare Strings by Count of Characters.

Create a function that takes two strings as arguments and return either
True or False depending on whether the total number of characters in the
first string is equal to the total number of characters in the second string.

Source:
https://edabit.com/challenge/C3N2JEfFQoh4cqQ98
"""


def comp(txt1: str, txt2: str) -> bool:
    """Compare string lengths."""
    return len(txt1) == len(txt2)


def main():
    """Run sample comp functions. Do not import."""
    assert comp("AB", "CD") is True
    assert comp("ABC", "DE") is False
    assert comp("hello", "edabit") is False
    assert comp("meow", "woof") is True
    assert comp("jrnvjrnnt", "cvjknfjvmfvnfjn") is False
    assert comp("jkvnjrt", "krnf") is False
    assert comp("Facebook", "Snapchat") is True
    print('Passed.')


if __name__ == "__main__":
    main()
