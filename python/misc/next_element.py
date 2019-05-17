#!/usr/bin/env python3

"""Next Element - Next Element in Arithmetic Sequence.

Create a function that returns the next element in an arithmetic sequence.
In an arithmetic sequence, each element is formed by adding the same constant
to the previous element.

Source:
https://edabit.com/challenge/CDqMdrTvfn2Wa8igp
"""

from typing import List, Union
from collections import namedtuple

ArithmeticSequence = namedtuple("ArithmeticSequence", ["arithmetic_sequence",
                                                       "msg",
                                                       "step"])


def is_arithmetic_sequence(sequence: List) -> (bool, str, Union[int, object]):
    """Determine if the sequence is an Arithmetic Sequence."""
    if not(len(sequence) >= 2):
        return ArithmeticSequence(False,
                                  f"Sequence '{sequence}' is too short.",
                                  object(),)
    step = sequence[1] - sequence[0]
    for index, element in enumerate(sequence[1:], start=2):
        if index < len(sequence) and not(sequence[index] - element == step):
            return ArithmeticSequence(False,
                                      f"Sequence '{sequence}' different constant in sequence.",
                                      object())
    return ArithmeticSequence(True, "", step,)


def next_element(sequence: List)-> int:
    """Given a Arithmetic Sequence, find the next element."""
    # Test if sequence is an arithmetic sequence.
    # find_next_element is True proceed to finding next element
    # else raise ArithmeticError with msg.
    arithmetic_sequence, msg, step = is_arithmetic_sequence(sequence)
    if not(arithmetic_sequence):
        raise ArithmeticError(f"{msg}")
    # Check to see if step is an integer.
    if not(isinstance(step, int)):
        raise TypeError(f"The 'step' value is not type int.")
    next_ = sequence[-1] + step
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
