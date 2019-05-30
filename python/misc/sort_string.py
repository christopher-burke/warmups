#!/usr/bin/env python3

"""Sort String.

Sort a string with this order:
    1. Punctuation
    2. Lowercase
    3. Uppercase
"""


def sort_string(text: str) -> str:
    """Sort string punctuation, lowercase and then uppercase."""
    return ''.join(sorted([x for x in text], key=str.swapcase))


def main():
    """Run sample sort_string functions. Do no import."""
    print(sort_string(text="Python string."))
    print(sort_string(text="DinningRoomChair"))
    print(sort_string(text="SunsetOnTheBeach"))
    print(sort_string(text="ABCcba"))


if __name__ == "__main__":
    main()
