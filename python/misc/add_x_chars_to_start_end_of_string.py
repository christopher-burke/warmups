#!/usr/bin/env python3

"""Add x Characters to the Start and End of a String.

Create a function that takes a string, a character and a length and returns
(length) characters before and after the string.

Source:
https://edabit.com/challenge/Drm6feac5QqBQz3bL
"""


def add_txt_n_char(txt: str,char: str, length:int ) -> str:
    """Create a new string with char of length bookending txt."""
    a = f'{char*length}'
    return f'{a}{txt}{a}'

def main():
    """. Do not import."""
    assert add_txt_n_char("John","*",4) == "****John****"
    print('Passed.')

if __name__ == "__main__":
    main()