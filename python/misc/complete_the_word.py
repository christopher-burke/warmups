#!/usr/bin/env python3

"""Complete the Word.

An input string can be completed if
additional letters can be added and
no letters need to be taken away to
match the word.

Furthermore, the order of the
letters in the input string must be
the same as the order of letters
in the final word.

Create a function that, given an input string,
determines if the word can be completed.


Source:
https://edabit.com/challenge/bd2fLqAxHfGTx86Qx
"""

from itertools import zip_longest


def can_complete(input_: str, word: str) -> bool:
    """Determine if word can be completed from input_."""
    input_ordered = enumerate(input_)
    letter_check = [letter
                    for start_index, letter in input_ordered
                    if letter in word[start_index:]]
    order_check = []
    input_list = list(input_)

    for letter in word:
        if letter in input_list:
            order_check.append(letter)
            input_list.pop(input_list.index(letter))

    return all([i[0] == i[1] and j[0] == j[1]
                # Check letters from input_ match word.
                for i in zip_longest(input_, letter_check)
                # Check the order of input_.
                for j in zip_longest(input_, order_check)
                ])


def main():
    """Run sample can_complete functions. Do not import."""
    assert can_complete("butl", "beautiful") is True
    assert can_complete("butlz", "beautiful") is False
    assert can_complete("tulb", "beautiful") is False
    assert can_complete("bbutl", "beautiful") is False
    assert can_complete('sg', 'something') is True
    assert can_complete('sgi', 'something') is False
    assert can_complete('sing', 'something') is True
    assert can_complete('siing', 'something') is False
    print('Passed.')


if __name__ == "__main__":
    main()
