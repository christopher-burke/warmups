#!/usr/bin/env python3

"""Password generator."""

import argparse
from string import printable, ascii_letters
from random import randint
from itertools import islice


def random_int() -> int:
    """Random integer generator."""
    while True:
        yield randint(0, 51)


def generate_password(strength: str) -> str:
    """Generate a strong or weak random password."""
    if strength == 'strong':
        selected = [i for i in islice(random_int(), 0, randint(12, 50))]
        return "".join(list(map(printable.__getitem__, selected)))
    else:
        selected = [i for i in islice(random_int(), 0, 8)]
        return "".join(list(map(ascii_letters.__getitem__, selected)))


def main() -> str:
    """Run Password generator as a script."""
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--strength", required=True,
                    help="Strong or Weak password")
    args = vars(ap.parse_args())
    strength = args['strength']
    print(f"You requested a {strength} password.".format())
    return generate_password(strength=strength.lower())


if __name__ == "__main__":
    print(main())
