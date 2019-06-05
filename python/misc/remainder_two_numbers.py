#!/usr/bin/env python3

"""Return the Remainder from Two Numbers.

There is a single operator in Python capable of providing the remainder of a
division operation. Two numbers are passed as parameters.
The first provider divided by the second parameter will
have a remainder, possibly zero. Return that value.

Source:
https://edabit.com/challenge/KWoj7kWiHRqJtG6S2
"""


def remainder(num1: int, num2: int) -> int:
    """Find the remainder from num1 and num2."""
    if all((num1 > 0, num2 >= 1,)):
        return num1 % num2
    raise ValueError("Check number inputs. ")


def main():
    print(remainder(1, 3))
    print(remainder(5, 5))
    print(remainder(7, 2))


if __name__ == "__main__":
    main()
