#!/usr/bin/env python3

"""Additive Inverse.

A number added with its additive inverse equals zero.
Create a function that returns a list of additive inverses.

Source:
https://edabit.com/challenge/nZTLizuJjLPgr7Ak2
"""


def additive_inverse(iterable: list) -> list:
    """Find the additive inverse of the iterable."""
    return [i * -1 for i in iterable]


def main():
    """Run sample additive_inverse functions. Do not import."""
    print(additive_inverse([5, -7, 8, 3]))
    print(additive_inverse([1, 1, 1, 1, 1]))
    print(additive_inverse([-5, -25, 35]))


if __name__ == "__main__":
    main()
