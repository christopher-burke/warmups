#!/usr/bin/env python3

"""First Before Second Letter.

You are given three inputs: a string, one letter, and a second letter.

Write a function that returns True if every instance
of the first letter occurs before every instance of the second letter.


Source:
https://edabit.com/challenge/D6XfxhRobdQvbKX4v
"""

import re


def first_before_second(str_in: str, first: str, second: str) -> bool:
    """Return True if every `first` occurs before every `second`."""
    return not bool(re.findall(f"{second}.*{first}", str_in))


def main():
    """Run sample first_before_second functions. Do not import."""
    assert first_before_second("a rabbit jumps joyfully", "a", "j") is True
    assert first_before_second(
        "knaves knew about waterfalls", "k", "w") is True
    assert first_before_second("maria makes money", "m", "o") is True
    assert first_before_second("the hostess made pecan pie", "h", "p") is True
    assert first_before_second(
        "barry the butterfly flew away", "b", "f") is True
    assert first_before_second("moody muggles", "m", "g") is True
    assert first_before_second("happy birthday", "a", "y") is False
    assert first_before_second("precarious kangaroos", "k", "a") is False
    assert first_before_second("maria makes money", "m", "i") is False
    assert first_before_second(
        "taken by the beautiful sunrise", "u", "s") is False
    assert first_before_second("sharp cheddar biscuit", "t", "s") is False
    assert first_before_second("moody muggles", "m", "o") is False
    print("Passed.")


if __name__ == "__main__":
    main()
