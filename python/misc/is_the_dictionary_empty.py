#!/usr/bin/env python3

"""Is the Dictionary Empty.

Write a function that returns True if a dictionary is empty, and False
otherwise.

Source:
https://edabit.com/challenge/CAgmHcypCLFDSadGp
"""


def is_empty(dictionary) -> bool:
    """Determine if the dictionary is empty."""
    return not(bool(dictionary))


def main():
    """Run sample functions. Do not import."""
    assert is_empty({}) is True
    assert is_empty({'a': 1}) is False
    assert is_empty({'z': 2, 'w': 4, 'y': 5}) is False
    print("Passed.")


if __name__ == "__main__":
    main()
