#!/usr/bin/env python3

"""Linked Lists - Add Two Integers.

Given the head pointers of two linked lists where each linked list represents
an integer number (each node is a digit), add them and return the
resulting linked list.

The first node in a list represents the least significant digit.
"""

from itertools import zip_longest
from typing import List


def add_two_integers(integer1: List, integer2: List) -> List:
    """Add two interger linked list."""
    result = []
    carry = 0
    for i in zip_longest(integer1, integer2, fillvalue=0):
        digit = sum(i) + carry
        if digit >= 10:
            carry = digit % 10
            if carry == 0:
                carry = 1
            digit = digit - 10
        result.append(digit)
    if carry > 0:
        result.append(carry)
    return result


def main():
    answer = add_two_integers(
        integer1=[1, 0, 9, 9, ],
        integer2=[7, 3, 2, ]
    )
    print(answer)


if __name__ == "__main__":
    main()
