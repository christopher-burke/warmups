#!/usr/bin/env python3

"""Sandwich Fillings

Given a sandwich (as a list), return a list of fillings inside the sandwich.
This involves ignoring the first and last elements.

Source:
https://edabit.com/challenge/T3p8AkyXcE9ALkWbA
"""

from typing import List

def get_fillings(sandwich: List) -> List:
    """Given a sandwich, return the ingredients."""
    return sandwich[1:-1]


def main():
    """Run sample get_fillings. Do not import."""
    assert get_fillings(['bread', 'ham', 'cheese', 'ham', 'bread']) == ['ham', 'cheese', 'ham']
    assert get_fillings(['bread', 'sausage', 'tomato', 'bread']) == ['sausage', 'tomato']
    assert get_fillings(['bread', 'lettuce', 'bacon', 'tomato', 'bread']) == ['lettuce', 'bacon', 'tomato']
    assert get_fillings(['bread', 'bacon', 'lettuce', 'tomato', 'bread']) == ['bacon', 'lettuce', 'tomato']
    assert get_fillings(['bread', 'tomato', 'tomato', 'ham', 'sausage', 'bread']) == ['tomato', 'tomato', 'ham', 'sausage']
    assert get_fillings(['bread', 'lettuce', 'bread']) == ['lettuce']
    assert get_fillings(['bread', 'cheese', 'bread']) == ['cheese']
    assert get_fillings(['bread', 'lettuce', 'tomato', 'ham', 'bread']) == ['lettuce', 'tomato', 'ham']
    assert get_fillings(['bread', 'ham', 'cheese', 'lettuce', 'ham', 'bread']) == ['ham', 'cheese', 'lettuce', 'ham']
    assert get_fillings(['bread', 'lettuce', 'lettuce', 'bread']) == ['lettuce', 'lettuce']
    assert get_fillings(['bread', 'sausage', 'ham', 'bread']) == ['sausage', 'ham']
    assert get_fillings(['bread', 'bacon', 'bread']) == ['bacon']
    assert get_fillings(['bread', 'ham', 'bread']) == ['ham']
    assert get_fillings(['bread', 'ham', 'bread']) == ['ham']
    assert get_fillings(['bread', 'sausage', 'ham', 'lettuce', 'bread']) == ['sausage', 'ham', 'lettuce']
    assert get_fillings(['bread', 'sausage', 'bread']) == ['sausage']
    assert get_fillings(['bread', 'lettuce', 'bread']) == ['lettuce']
    assert get_fillings(['bread', 'tomato', 'lettuce', 'cheese', 'cheese', 'bread']) == ['tomato', 'lettuce', 'cheese', 'cheese']
    assert get_fillings(['bread', 'tomato', 'sausage', 'bacon', 'tomato', 'bread']) == ['tomato', 'sausage', 'bacon', 'tomato']
    assert get_fillings(['bread', 'bacon', 'ham', 'lettuce', 'tomato', 'lettuce', 'bread']) == ['bacon', 'ham', 'lettuce', 'tomato', 'lettuce']
    assert get_fillings(['bread', 'tomato', 'lettuce', 'cheese', 'lettuce', 'bread']) == ['tomato', 'lettuce', 'cheese', 'lettuce']
    assert get_fillings(['bread', 'ham', 'ham', 'bacon', 'ham', 'cheese', 'bread']) == ['ham', 'ham', 'bacon', 'ham', 'cheese']
    assert get_fillings(['bread', 'tomato', 'bacon', 'ham', 'tomato', 'bread']) == ['tomato', 'bacon', 'ham', 'tomato']
    assert get_fillings(['bread', 'ham', 'cheese', 'lettuce', 'bread']) == ['ham', 'cheese', 'lettuce']
    assert get_fillings(['bread', 'lettuce', 'bread']) == ['lettuce']
    assert get_fillings(['bread', 'lettuce', 'bacon', 'bacon', 'bread']) == ['lettuce', 'bacon', 'bacon']
    assert get_fillings(['bread', 'tomato', 'cheese', 'sausage', 'bread']) == ['tomato', 'cheese', 'sausage']
    assert get_fillings(['bread', 'cheese', 'ham', 'bread']) == ['cheese', 'ham']
    assert get_fillings(['bread', 'tomato', 'bread']) == ['tomato']
    assert get_fillings(['bread', 'sausage', 'bread']) == ['sausage']
    assert get_fillings(['bread', 'cheese', 'bread']) == ['cheese']
    assert get_fillings(['bread', 'ham', 'bacon', 'sausage', 'lettuce', 'sausage', 'bread']) == ['ham', 'bacon', 'sausage', 'lettuce', 'sausage']
    assert get_fillings(['bread', 'cheese', 'lettuce', 'lettuce', 'bacon', 'lettuce', 'bread']) == ['cheese', 'lettuce', 'lettuce', 'bacon', 'lettuce']
    assert get_fillings(['bread', 'bacon', 'sausage', 'ham', 'bacon', 'bread']) == ['bacon', 'sausage', 'ham', 'bacon']
    assert get_fillings(['bread', 'bacon', 'tomato', 'bread']) == ['bacon', 'tomato']
    assert get_fillings(['bread', 'tomato', 'bread']) == ['tomato']
    assert get_fillings(['bread', 'cheese', 'cheese', 'tomato', 'bread']) == ['cheese', 'cheese', 'tomato']
    assert get_fillings(['bread', 'cheese', 'tomato', 'bread']) == ['cheese', 'tomato']
    assert get_fillings(['bread', 'lettuce', 'bread']) == ['lettuce']
    assert get_fillings(['bread', 'lettuce', 'sausage', 'bread']) == ['lettuce', 'sausage']
    assert get_fillings(['bread', 'tomato', 'tomato', 'bread']) == ['tomato', 'tomato']
    assert get_fillings(['bread', 'tomato', 'lettuce', 'cheese', 'bacon', 'bread']) == ['tomato', 'lettuce', 'cheese', 'bacon']
    assert get_fillings(['bread', 'tomato', 'lettuce', 'bread']) == ['tomato', 'lettuce']
    assert get_fillings(['bread', 'bacon', 'bacon', 'tomato', 'lettuce', 'bacon', 'bread']) == ['bacon', 'bacon', 'tomato', 'lettuce', 'bacon']
    assert get_fillings(['bread', 'sausage', 'sausage', 'lettuce', 'bread']) == ['sausage', 'sausage', 'lettuce']
    assert get_fillings(['bread', 'ham', 'bacon', 'ham', 'ham', 'bread']) == ['ham', 'bacon', 'ham', 'ham']
    assert get_fillings(['bread', 'lettuce', 'cheese', 'lettuce', 'bread']) == ['lettuce', 'cheese', 'lettuce']
    assert get_fillings(['bread', 'ham', 'sausage', 'cheese', 'tomato', 'bread']) == ['ham', 'sausage', 'cheese', 'tomato']
    assert get_fillings(['bread', 'ham', 'cheese', 'bacon', 'bread']) == ['ham', 'cheese', 'bacon']
    assert get_fillings(['bread', 'cheese', 'tomato', 'bread']) == ['cheese', 'tomato']
    assert get_fillings(['bread', 'bacon', 'lettuce', 'ham', 'tomato', 'lettuce', 'bread']) == ['bacon', 'lettuce', 'ham', 'tomato', 'lettuce']
    assert get_fillings(['bread', 'ham', 'bacon', 'bread']) == ['ham', 'bacon']
    assert get_fillings(['bread', 'ham', 'lettuce', 'bread']) == ['ham', 'lettuce']
    print('Passed.')

if __name__ == "__main__":
    main()