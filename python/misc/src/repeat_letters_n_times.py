#!/usr/bin/env python3

"""Repeating Letters N Times.

Create a function that repeats each character in a string n times.

Source:
https://edabit.com/challenge/mZyHqasaNyFp23RcS
"""


def repeat(text: str, n: int) -> str:
    """Repeat each character in a string n times."""
    return "".join([letter * n for letter in text])


def main():
    """Run sample repeat functions."""
    print(repeat("mice", 5))
    print(repeat("hello", 3))
    print(repeat("stop", 1))


if __name__ == "__main__":
    main()
