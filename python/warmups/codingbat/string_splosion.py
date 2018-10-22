#!/usr/bin/env python3


"""Given a non-empty string like "Code" 
return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

source: https://codingbat.com/prob/p118366
"""


def string_splosion(str_: str) -> str:
    """Return a string with each subsequence spelled out.

    examples: 
            Code -> 'CCoCodCode'
            Math -> 'MMaMatMath'
            Program -> 'PPrProProgProgrPrograProgram'

    :return: string splosion of original string."""
    l = len(str_)
    return_string = ""
    for i in range(l, 0, -1):
        return_string = str_[:i] + return_string

    return return_string


def main():
    print(string_splosion('Program'))
    assert string_splosion('Code') == 'CCoCodCode'
    assert string_splosion('abc') == 'aababc'
    assert string_splosion('ab') == 'aab'
    assert string_splosion('x') == 'x'
    assert string_splosion('fade') == 'ffafadfade'
    assert string_splosion('There') == 'TThTheTherThere'
    assert string_splosion('Kitten') == 'KKiKitKittKitteKitten'
    assert string_splosion('Bye') == 'BByBye'
    assert string_splosion('Good') == 'GGoGooGood'
    assert string_splosion('Bad') == 'BBaBad'
    print('Passed.')


if __name__ == "__main__":
    main()
