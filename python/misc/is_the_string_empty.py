#!/usr/bin/env python3

"""Is the string empty.

Create a function that returns True if a string is empty and
False otherwise.

Source:
https://edabit.com/challenge/wtu32ZFxHJsuQnogX
"""


def is_empty(s: str) -> bool:
    """Test the if the string is empty."""
    return not bool(s)


def main():
    """Run sample is_empty functions. Do not import."""
    assert is_empty("") is True
    assert is_empty(" ") is False
    assert is_empty("            ") is False
    assert is_empty("38215") is False
    assert is_empty("afjabsdf") is False
    assert is_empty("!?@&") is False
    print('Passed.')


if __name__ == "__main__":
    main()
