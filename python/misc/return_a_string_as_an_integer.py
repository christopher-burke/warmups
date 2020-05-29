#!/usr/bin/env python3

"""Return a String as an Integer.

Create a function that takes a string and returns it as an integer.

Source:
https://edabit.com/challenge/GPmoRCZKkyNtoJMcN
"""


def string_int(txt: str) -> int:
    """Convert string to int."""
    return int(txt)


def main():
    """Run sample string_int functions. Do not import."""
    assert string_int("6") == 6
    assert string_int("2") == 2
    assert string_int("10") == 10
    assert string_int("666") == 666
    print('Passed.')

if __name__ == "__main__":
    main()