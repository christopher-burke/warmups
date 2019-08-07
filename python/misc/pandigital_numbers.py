#!/usr/bin/env python3

"""Pandigital Numbers.

A pandigital number contains all digits (0-9) at least once. Write a function that takes an integer, 
returning True if the integer is pandigital, and False otherwise.

Source:
https://edabit.com/challenge/x44ZRvQtJ6TyZQhwx
"""


def is_pandigital(n: int) -> bool:
    """Determine if n is pandigital."""
    lst = set(sorted([int(i) for i in str(n)]))
    return len(lst) == 10


def main():
    """Run sample is_pandigital functions. Do not import."""
    assert is_pandigital(123456789876543210) is True
    assert is_pandigital(546732965015) is False
    assert is_pandigital(6781235184590) is True
    assert is_pandigital(9432821089765) is True
    assert is_pandigital(678798215643817) is False
    assert is_pandigital(90864523148909) is False
    assert is_pandigital(112233445566778899) is False
    assert is_pandigital(647380265483206) is False
    assert is_pandigital(38165975424790) is True
    assert is_pandigital(8146327815320) is False
    assert is_pandigital(768431605430) is False
    assert is_pandigital(4920124852367763) is True
    assert is_pandigital(60543981597247) is True
    assert is_pandigital(10282343456789) is True
    print('Passed.')


if __name__ == "__main__":
    main()
