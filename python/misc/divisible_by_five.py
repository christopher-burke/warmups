#!/usr/bin/env python3

"""Check if an Integer is Divisible By Five.

Create a function that returns True if an integer is divisible by 5,
and false otherwise.

Source:
https://edabit.com/challenge/49pyDP8dE3pJ2dYMW
"""


def divisible_by_five(n: int) -> bool:
    """Return True if an integer is divisible by 5, and false otherwise."""
    if n % 5 > 0:
        return False
    return True


def main():
    """Run sample divisible_by_five functions. Do not import."""
    assert divisible_by_five(7) is False
    assert divisible_by_five(5) is True
    assert divisible_by_five(15) is True
    assert divisible_by_five(33) is False
    assert divisible_by_five(-18) is False
    assert divisible_by_five(999) is False
    assert divisible_by_five(2) is False
    print('Passed.')


if __name__ == "__main__":
    main()
