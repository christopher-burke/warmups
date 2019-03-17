#!/usr/bin/env python3

"""Slice of Pie.

Create a function that determines whether or not it's possible
to split a pie fairly given these three parameters:

Total number of slices.
Number of recipients.
How many slices each person gets.

Source:
https://edabit.com/challenge/fqn5FcLzEb4RBH9w7
"""


def equal_slices(total_slices: int, people: int, slices: int) -> bool:
    """Determine if the number of slices to people can work."""
    if (people * slices) > total_slices:
        return False
    return True


def main():
    """Run equal_slices with samples."""
    print(equal_slices(11, 5, 2))
    print(equal_slices(11, 5, 3))
    print(equal_slices(8, 3, 2))
    print(equal_slices(8, 3, 3))
    print(equal_slices(24, 12, 2))


if __name__ == "__main__":
    main()
