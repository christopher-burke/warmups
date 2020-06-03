#!/usr/bin/env python3

"""Modifying the Last Character.

Create a function which makes the last character of a string repeat n
number of times.

Source:
https://edabit.com/challenge/MWM3f4aKjPacPt2zw
"""


def modify_last(txt: str, n: int) -> str:
    """String with last character repeated n times."""
    return f"{txt[:-1]}{txt[-1]*n}"


def main():
    """Run sample functions. Do not import."""
    assert modify_last("Hello", 3) == "Hellooo"
    assert modify_last("hey", 6) == "heyyyyyy"
    assert modify_last("plsssss!1!", 5) == "plsssss!1!!!!!"
    assert modify_last("gr", 2) == "grr"
    assert modify_last("excuse me what?", 5) == "excuse me what?????"
    assert modify_last("123", 5) == "1233333"
    assert modify_last("a", 3) == "aaa"
    assert modify_last("STOP", 3) == "STOPPP"
    print('Passed.')

if __name__ == "__main__":
    main()