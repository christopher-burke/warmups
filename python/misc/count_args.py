#!/usr/bin/env python3

"""Count the Arguments.

Create a function that returns the number of argument it was called with.

Source:
https://edabit.com/challenge/QXrpKvEvJA2Yxj2fo
"""


def num_args(*args):
    """Return the number of arguments called."""
    return len(args)


def main():
    """Run sample num_args functions."""
    print(num_args())
    print(num_args("foo"))
    print(num_args("foo", "bar"))
    print(num_args(True, False))
    print(num_args({}))

    pass


if __name__ == "__main__":
    main()
