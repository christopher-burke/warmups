#!/usr/bin/env python3


"""Largest Palindrom Product.

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is:
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

source: https://projecteuler.net/problem=4
"""


def palindrome(number: int) -> bool:
    """Determine if number is a palindrome.

    :return: True if palindrome, False otherwise.
    """
    str_number = str(number)
    reverse = str_number[::-1]
    return True if str_number == reverse else False


def three_digit_palindrome_product():
    """Find the largest three digit palindrome product.

    :return: Tuple of the ((palindrome), (factors),)
    """
    palindrome_max = 0
    factors = []
    for i in range(999, 100, -1):
        for j in range(i - 99, i + 1):
            num = i*j
            if palindrome(num) and num > palindrome_max:
                palindrome_max = num
                factors = (i, j,)
    return ((palindrome_max,), factors,)


def main():
    """Run the program."""
    return three_digit_palindrome_product()


if __name__ == "__main__":
    print(main())
