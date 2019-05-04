#!/usr/bin/env python3

"""Character to ASCII.

Create a function that returns the ASCII
value of the passed in character.

Source:
https://edabit.com/challenge/9wfEZ4898nnpa9wL5
"""


def ctoa(character: str) -> int:
    """Find the ASCII value of character.

    Uses the ord builtin function.
    """
    code = ord(character)
    return code


def main():
    """Run samples."""
    print(ctoa("A"))
    print(ctoa("m"))
    print(ctoa("["))
    print(ctoa("\\"))


if __name__ == "__main__":
    main()
