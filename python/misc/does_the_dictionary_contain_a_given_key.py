#!/usr/bin/env python3

"""Does the Dictionary Contain a Given Key.

Write a function that returns True if a dictionary contains the specified key,
and False otherwise.

Source:
https://edabit.com/challenge/zdo6JCL6Z5d2fT8JB
"""

def has_key(dictionary, key) -> bool:
    """Dictionary contain the key."""
    return key in dictionary.keys()


def main():
    """Run sample functions. Do not import."""
    assert has_key({"pot": 1, "tot": 2, "not": 3}, "not") is True
    assert has_key({"craves": True, "midnight": True, "snack": True}, "morning") is False
    assert has_key({"a": 44, "b": 45, "c": 46}, "d") is False
    assert has_key({"a": "z", "b": "y", "c": "x"}, "c") is True
    print('Passed.')

if __name__ == "__main__":
    main()