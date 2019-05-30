#!/usr/bin/env python3

"""Split usernames.

Usernames consist of first initial and last name. If there
more than 1 record exists for a given username a number is appended
to the end of the name. Write a function that splits the username (alpha chars)
from its digits (numberic).
"""

from typing import Tuple
import re


def split_username(username: str) ->Tuple[str, str]:
    r"""Split the alpha characters from the numberic characters.

    Usernames follow the following pattern:  \w+\d*

    Return a tuple containing the username alpha characters and
    numberic characters respectively.
    """
    split = re.compile(r"\d+")
    match = split.search(username)
    start = match.start() if match else len(username)

    return (username[:start], username[start:])


def main():
    """Run sample split_username functions. Do not import."""
    print(split_username('jdoe123'))
    print(split_username('jsmith5'))
    print(split_username('ganderson5'))
    print(split_username('dprince'))
    print(split_username('ckent4'))


if __name__ == "__main__":
    main()
