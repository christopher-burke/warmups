#!/usr/bin/env python3

"""Concatenate First and Last Name into One String.

Given two strings, first_name and last_name, return a 
single string in the format "last, first".

Source:
https://edabit.com/challenge/pFQPcaaASgHuACbaS
"""


def concat_name(first_name: str, last_name: str) -> str:
    """Return new string 'last_name, first_name'."""
    return f"{last_name}, {first_name}"


def main():
    """Run sample concat_name functions. Do not import."""
    assert concat_name("John", "Doe") == "Doe, John"
    assert concat_name("First", "Last") == "Last, First"
    assert concat_name("A", "B") == "B, A"
    # In case someone is making odd assumptions about comma characters.
    assert concat_name(",", ",") == ",, ,"
    print('Passed.')


if __name__ == "__main__":
    main()
