#!/usr/bin/env python3

"""Equality of 3 Values.

Create a function that takes three integer arguments (a, b, c)
and returns the number of equal values.

Source:
https://edabit.com/challenge/b8wRDMWgMZTN2nmfx
"""


def equal(a: int, b: int, c: int):
    """Return the number of equal values in (a,b,c)."""
    test_equality = set([a, b, c])
    length = len(test_equality)
    count = int(length % 3)
    number_of_equal_values = 3 if count is 1 else count
    return number_of_equal_values


def main():
    """Test equal function. Do Not Import."""
    print(equal(3, 4, 3))
    print(equal(1, 1, 1))
    print(equal(3, 4, 1))


if __name__ == "__main__":
    main()
