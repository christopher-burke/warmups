#!/usr/bin/env python3

"""Using the "and" Operator.

Make a function using the and operator.

Source:
https://edabit.com/challenge/gbWDtMHtZARm7sdNA
"""


def And(*args) -> bool:
    """Logical and operator."""
    return all(args)

def main():
    """Run sample And functions. Do not import."""
    assert And(True, True) == True
    assert And(True, False) == False
    assert And(False, True) == False
    assert And(False, False) == False
    print('Passed.')

if __name__ == "__main__":
    main()