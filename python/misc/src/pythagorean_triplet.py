#!/usr/bin/env python3

"""Pythagorean Triplet.


Given an array of integers, write a function that returns 
true if there is a triplet (a, b, c) that satisfies 
a**2 + b**2 = c**2.

source: https://practice.geeksforgeeks.org/problems/pythagorean-triplet/0

"""


def main(A):
    """Pythagorean Triplet in Array A."""
    squares = sorted([x**2 for x in A])
    for x in reversed(squares):
        for y in squares[0:
                         squares.index(x)]:
            if x - y in squares[squares.index(y):
                                squares.index(x)]:
                return True

    return False


if __name__ == "__main__":
    print(main(A=[3, 2, 4, 6, 5, ]))
    print(main(A=[3, 2, 4, 6, ]))
    print(main(A=[3, 1, 4, 6, 5, ]))
