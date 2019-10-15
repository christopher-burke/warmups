#!/usr/bin/env python3

"""String to Integer and Vice Versa.

Write two functions:

    to_int() : A function to convert a string to an integer.
    to_str() : A function to convert an integer to a string.

Source:
https://edabit.com/challenge/WKJwo2xDNjKxwtGoH
"""


def to_int(string: str) -> int:
    """Convert a string to an integer."""
    return int(string)


def to_str(num: int) -> str:
    """Convert an integer to a string."""
    return str(num)


def main():
    """Run sample to_int and to_str functions. Do not import."""
    assert to_int("37") == 37
    assert to_int("113") == 113
    assert to_int("5") == 5
    assert to_int("5231") == 5231
    assert to_str(37) == "37"
    assert to_str(113) == "113"
    assert to_str(5) == "5"
    assert to_str(5231) == "5231"
    print('Passed.')


if __name__ == "__main__":
    main()
