#!/usr/bin/env python3

"""


You are to read each part of the date into its own integer type variable.
The year should be a 4 digit number. You can assume the user enters a correct
date (no error checking required).

Determine whether the entered date is a magic date.
Here are the rules for a magic date:

* mm * dd is a 1-digit number that matches the last digit of yyyy or
* mm * dd is a 2-digit number that matches the last 2 digits of yyyy or
* mm * dd is a 3-digit number that matches the last 3 digits of yyyy

The program should then display True or False.
True if the date is magic, or False if it is not.

Source:
https://edabit.com/challenge/GoGbZtXDYPDCfeBz8
"""

import math


def magic(date: str):
    """Determine if date entered is a magic date.

    Uses math.log10 to determine the length of digits in product.
    """
    month, date_, year = date.split(' ')
    month, date_ = int(month), int(date_)
    mm_dd_product = month * date_
    lenth_product = (int(math.log10(mm_dd_product))+1) * -1
    return mm_dd_product == int(year[lenth_product:])


def main():
    """Print tests for magic function. Do not import."""
    print(magic('1 1 2011'), True, 'magic date')
    print(magic('4 1 2001'), False, 'is not a magic date')
    print(magic('2 4 2008'), True, 'magic date')
    print(magic('3 3 2009'), True, 'magic date')
    print(magic('5 2 2010'), True, 'magic date')
    print(magic('1 2 2011'), False, 'is not a magic date')
    print(magic('9 2 2011'), False, 'is not a magic date')
    print(magic('1 4 2011'), False, 'is not a magic date')


if __name__ == "__main__":
    main()
