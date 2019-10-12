#!/usr/bin/env python3

"""Create random usernames.

Create usernames using the following:
    * First letter of the first name.
    * First five (5) characters of the last name.
    * A random number between 10 to 99 (inclusive).
"""


import random


def create_username(first_name: str, last_name: str, seed: int=None) -> str:
    """Create a username based on the first and last name given."""
    return f"{first_name[0].lower()}{last_name[0:5].lower()}{random.randrange(10,100)}"


def main():
    """Run sample create_username functions, Do not import.

    Random is seeded with 10.
    """
    random.seed(10)
    assert create_username(first_name="Johnny",
                           last_name="Appleseed") == "japple83"
    assert create_username(first_name="Paul", last_name="Bunyan") == "pbunya14"
    assert create_username(first_name="Thomas",
                           last_name="Sawyer") == "tsawye64"
    assert create_username(
        first_name="Henry", last_name="Jekyll") == "hjekyl71"
    print('Passed.')


if __name__ == "__main__":
    main()
