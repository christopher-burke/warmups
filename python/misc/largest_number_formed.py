#!/usr/bin/env python3

"""Largest Number formed from an Array.

Given a list of non negative integers,
arrange them in such a manner that they
form the largest number possible.
The result is going to be very large,
hence return the result in the form of a string.

Soruce:
https://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array/0
"""


from itertools import permutations


def largest_number(items: list) -> int:
    """Find the largest number formed in a list.

    Uses itertools permutations.
    """
    permutations_ = []
    for i in permutations(items, len(items)):
        permutations_.append(int("".join(map(str, i))))
    return max(permutations_)


def main():
    """Run largest number functions."""
    print(largest_number(items=[3, 30, 34, 5, 9, ]))
    print(largest_number(items=[54, 546, 548, 60, ]))


if __name__ == "__main__":
    main()
