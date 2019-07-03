#!/usr/bin/env python3

"""Pentagonal Number

Write a function that takes a positive integer and calculates how
many dots exist in a pentagonal shape around the center dot
on the Nth iteration.

Source:
https://edabit.com/challenge/st8mDxreMcuWxuz8c

"""


def pentagonal(n: int) -> int:
    """Find the number of dots in nth pentagonal number."""
    # Find the pentagonal number to nth degree.
    pentagonal_number = (n * ((3 * n) - 1) // 2)

    # Find the total number of dots.
    dots = ((n-1) ** 2)
    dots += pentagonal_number
    return dots


def main():
    """Run sample pentagonal sample functions. Do Not Import."""
    print(pentagonal(1))
    print(pentagonal(2))
    print(pentagonal(3))
    print(pentagonal(8))


if __name__ == "__main__":
    main()
