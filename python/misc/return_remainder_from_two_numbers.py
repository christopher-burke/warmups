#!/usr/bin/env python3

"""Return the Remainder from Two Numbers.

There is a single operator in Python, capable of providing the remainder of a
division operation. Two numbers are passed as parameters. The first parameter
divided by the second parameter will have a remainder, possibly zero.
Return that value.

Source:
https://edabit.com/challenge/KWoj7kWiHRqJtG6S2
"""


def remainder(x: int, y: int) -> int:
    """Return the remainder of x/y."""
    return x % y


def main():
    """Run sample remainder functions. Do not import."""
    assert remainder(7, 2) == 1
    assert remainder(3, 4) == 3
    assert remainder(5, 5) == 0
    assert remainder(1, 3) == 1
    print('Passed.')


if __name__ == "__main__":
    main()
