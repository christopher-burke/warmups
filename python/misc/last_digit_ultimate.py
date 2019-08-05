#!/usr/bin/env python3

"""Last Digit Ultimate.

Your job is to create a function, that takes 3 numbers:
a, b, c and returns True if the last digit of
(the last digit of a * the last digit of b) = the last digit of c.

Source:
https://edabit.com/challenge/7PtLRCT5aL9uiqxPs
"""


def last_dig(a: int, b: int, c: int) -> bool:
    """Determine if last digit of c equals last digit of a * b."""
    # Make list of list digits of a,b,c.
    last_digits = [digit % 10 for digit in [a, b, c, ]]
    # Calculate a*b and find the last digit.
    ab_last_digit = (last_digits[0] * last_digits[1]) % 10
    # Assign last digit of c to variable.
    c_last_digit = last_digits[2]
    # Compare ab_last_digit to c_last_digit and return.
    return ab_last_digit == c_last_digit


def main():
    """Run sample functions. Do not import."""
    assert last_dig(1, 1, 1) == True
    assert last_dig(12, 15, 10) == True
    assert last_dig(15228, 9209, 72162) == True
    assert last_dig(15, 1, 1) == False
    assert last_dig(123, 15, 10) == False
    assert last_dig(5213, 99219, 6165) == False
    assert last_dig(1523, 513, 512) == False
    assert last_dig(-15, 1, 1) == False
    assert last_dig(123, -15, 10) == False
    assert last_dig(-12, 15, -10) == True
    assert last_dig(15228, -9209, -72162) == True
    print('Passed.')


if __name__ == "__main__":
    main()
