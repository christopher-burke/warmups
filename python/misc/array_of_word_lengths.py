#!/usr/bin/env python3

"""Array of Word Lengths.

Create a function that takes a list of words and transforms it into a 
list of each word's length.

Source:
https://edabit.com/challenge/sTbmSqFX7HxAesWor
"""


def word_lengths(lst):
    """Return a list of word lengths."""
    return [len(str_) for str_ in lst]

def main():
    """Run sample word_lengths functions. Do not import."""
    assert word_lengths(["hello", "world"]) == [5, 5]
    assert word_lengths(["Halloween", "Thanksgiving", "Christmas"]) == [9, 12, 9]
    assert word_lengths(["She", "sells", "seashells", "down", "by", "the", "seashore"]) == [3, 5, 9, 4, 2, 3, 8]
    assert word_lengths(["Indiana", "Jones", "and", "the", "Temple", "of", "Doom"]) == [7, 5, 3, 3, 6, 2, 4]
    assert word_lengths(["Programming", "is", "fun"]) == [11, 2, 3]
    print('Passed.')

if __name__ == "__main__":
    main()