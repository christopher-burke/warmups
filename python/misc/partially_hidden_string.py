#!/usr/bin/env python3

"""Partially Hidden String.

Create a function that takes a phrase and transforms each word
using the following rules:

* Keep first and last character the same.
* Transform middle characters into a dash -.

Source:
https://edabit.com/challenge/h9hp2vGKbHJBzN87i
"""


def hide_word(word, replace_char='-'):
    """Hide the word."""
    return "".join([word[0], len(word[1:-1]) * replace_char, word[-1]])


def partially_hide(phrase):
    """Modify the phrase."""
    return " ".join([hide_word(word) for word in phrase.split()])


def main():
    """Run sample partially_hide functions. Do not import."""
    assert partially_hide('Harry went to fight the basilisk') == \
        'H---y w--t to f---t t-e b------k'
    assert partially_hide('She rolled her eyes') == \
        'S-e r----d h-r e--s'
    assert partially_hide('skies were so beautiful') == \
        's---s w--e so b-------l'
    assert partially_hide('red is not my color') == \
        'r-d is n-t my c---r'
    assert partially_hide('so many options') == \
        'so m--y o-----s'
    assert partially_hide('the orient express') == \
        't-e o----t e-----s'
    assert partially_hide('went to the post office') == \
        'w--t to t-e p--t o----e'
    print('Passed.')


if __name__ == "__main__":
    main()
