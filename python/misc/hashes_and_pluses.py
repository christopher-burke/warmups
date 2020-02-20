#!/usr/bin/env python3

"""Hashes and Pluses.

Create a function that returns the number of hashes and pluses in a string.

Source:
https://edabit.com/challenge/pYwnLBJHBbHaEEano
"""


def count(token: str, txt: str)-> int: 
    """Count the token in the txt."""
    return  txt.count(token)


def hash_plus_count(txt:str):
    """Count the hashes and pluses in the txt."""
    return [count(token='#', txt=txt), count(token='+',txt=txt)]

def main():
    """Run sample functions. Do not import."""
    assert hash_plus_count("####") == [4, 0]
    assert hash_plus_count("#") == [1, 0]
    assert hash_plus_count("+++++++") == [0, 7]
    assert hash_plus_count("++") == [0, 2]
    assert hash_plus_count("#+#+") == [2, 2]
    assert hash_plus_count("###+") == [3, 1]
    assert hash_plus_count("##+++#") == [3, 3]
    assert hash_plus_count("#+++#+#++#") == [4, 6]
    assert hash_plus_count("") == [0, 0]
    print('Passed.')

if __name__ == "__main__":
    main()