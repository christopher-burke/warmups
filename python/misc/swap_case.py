#!/usr/bin/env python3

"""Swap case.

Given a string, swap the letter cases. From lowercase to uppercase
and from uppercase to lowercase.

Source:
https://www.hackerrank.com/challenges/swap-case/problem
"""


def swap_case(text: str) -> str:
    """Swap the case of each letter in text.

    Uses list comprehension and Ternary operator.
    """
    buffer = [letter.upper()
              if letter.islower() else
              letter.lower()
              for letter in text]

    return "".join(buffer)


def main():
    print(swap_case("This is a sample string."))
    print(swap_case('wWw.someWEBSITE.com'))
    print(swap_case(''))
    print(swap_case('All YOUR BASE belong TO us'))


if __name__ == "__main__":
    main()
