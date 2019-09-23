#!/usr/bin/env python3

"""Count Letters in a Word Search.

Create a function that counts the number of times a particular
letter shows up in the word search.

Source:
https://edabit.com/challenge/GBv4nB8SzkAnrM3B9
"""


def letter_counter(lst: list, letter: str) -> int:
    """Count the number of times letter shows up in the word search."""
    return sum([1
                for row in lst
                for letters in row
                if letter == letters]
               )


def main():
    """Run sample letter_counter functions. Do not import."""
    assert letter_counter([
        ['D', 'E', 'Y', 'H', 'A', 'D'],
        ['C', 'B', 'Z', 'Y', 'J', 'K'],
        ['D', 'B', 'C', 'A', 'M', 'N'],
        ['F', 'G', 'G', 'R', 'S', 'R'],
        ['V', 'X', 'H', 'A', 'S', 'S']
    ], 'D') == 3

    assert letter_counter([
        ['D', 'E', 'Y', 'H', 'A', 'D'],
        ['C', 'B', 'Z', 'Y', 'J', 'K'],
        ['D', 'B', 'C', 'A', 'M', 'N'],
        ['F', 'G', 'G', 'R', 'S', 'R'],
        ['V', 'X', 'H', 'A', 'S', 'S']
    ], 'H') == 2

    assert letter_counter([
        ['D', 'E', 'Y', 'H', 'A', 'D'],
        ['C', 'B', 'Z', 'Y', 'J', 'K'],
        ['D', 'B', 'C', 'A', 'M', 'N'],
        ['F', 'G', 'G', 'R', 'S', 'R'],
        ['V', 'X', 'H', 'A', 'S', 'S']
    ], 'Z') == 1

    assert letter_counter([
        ['D', 'E', 'Y', 'H', 'A', 'D'],
        ['C', 'B', 'Z', 'Y', 'J', 'K'],
        ['D', 'B', 'C', 'A', 'M', 'N'],
        ['F', 'G', 'G', 'R', 'S', 'R'],
        ['V', 'X', 'H', 'A', 'S', 'S']
    ], 'R') == 2

    assert letter_counter([
        ['D', 'E', 'Y', 'H', 'A', 'D'],
        ['C', 'B', 'Z', 'Y', 'J', 'K'],
        ['D', 'B', 'C', 'A', 'M', 'N'],
        ['F', 'G', 'G', 'R', 'S', 'R'],
        ['V', 'X', 'H', 'A', 'S', 'S']
    ], 'X') == 1

    assert letter_counter([
        ['D', 'E', 'Y', 'H', 'A', 'D'],
        ['C', 'B', 'Z', 'Y', 'J', 'K'],
        ['D', 'B', 'C', 'A', 'M', 'N'],
        ['F', 'G', 'G', 'R', 'S', 'R'],
        ['V', 'X', 'H', 'A', 'S', 'S']
    ], 'S') == 3

    assert letter_counter([
        ['D', 'E', 'Y', 'H', 'A', 'D'],
        ['C', 'B', 'Z', 'Y', 'J', 'K'],
        ['D', 'B', 'C', 'A', 'M', 'N'],
        ['F', 'G', 'G', 'R', 'S', 'R'],
        ['V', 'X', 'H', 'A', 'S', 'S']
    ], 'O') == 0
    print('Passed.')


if __name__ == "__main__":
    main()
