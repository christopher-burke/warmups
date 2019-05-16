#!/usr/bin/env python3

"""Next Element - Next Element in Arithmetic Sequence.

Create a function that returns the next element in an arithmetic sequence.
In an arithmetic sequence, each element is formed by adding the same constant
to the previous element.

Source:
https://edabit.com/challenge/CDqMdrTvfn2Wa8igp
"""

from typing import List


def is_arithmetic_sequence(sequence: List) -> (bool, str):
    """Determine if the sequence is an Arithmetic Sequence."""
    if not(len(sequence) >= 2):
        return False, f"Sequence '{sequence}' is too short."
    step = sequence[1] - sequence[0]
    for index, element in enumerate(sequence[1:], start=2):
        if index < len(sequence) and not(sequence[index] - element == step):
            return False, f"Sequence '{sequence}' different constant in sequence."
    return True, ""


def next_element(sequence: List)-> int:
    """Given a Arithmetic Sequence, find the next element."""
    # Test if sequence is an arithmetic sequence.
    # find_next_element is True proceed to finding next element
    # else raise ArithmeticError with msg.
    find_next_element, msg = is_arithmetic_sequence(sequence)
    if not(find_next_element):
        raise ArithmeticError(f"{msg}")
    arithmetic_sequence = sequence[-1] - sequence[-2]
    next_ = sequence[-1] + arithmetic_sequence
    return next_


def main():
    """Run sample next_element functions. Do not import."""
    print(next_element([3, 5, 7, 9, ]))
    print(next_element([-5, -6, -7, ]))
    print(next_element([2, 2, 2, 2, 2, ]))
    # Raise ArithmeticError - not Arithmetic Sequence
    try:
        next_element([2, 2, 2, 2, 22, ])
    except ArithmeticError as e:
        print(
            f"ArithmeticError: {e}"
        )
    # Raise ArithmeticError - sequence is too short
    try:
        next_element([1, ])
    except ArithmeticError as e:
        print(
            f"ArithmeticError: {e}"

        )


if __name__ == "__main__":
    main()
