#!/usr/bin/env python3

"""Change Every Letter to the Next Letter.

Source:
https://edabit.com/challenge/oiHH7qocTyM3JqNf8
"""

from string import ascii_lowercase


def move_letter(letter: str, moves: int) -> str:
    """Move letter based on the number of moves."""
    case = 'upper' if letter.isupper() else 'lower'
    index = ascii_lowercase.index(letter.lower())
    index = index + moves

    if index >= len(ascii_lowercase):
        index = index % len(ascii_lowercase)

    if case == 'upper':
        return ascii_lowercase[index].upper()
    return ascii_lowercase[index]


def move(str_input: str, moves: int=1) -> str:
    """Change every letter to the next letter."""
    output = []
    for i in str_input:
        moved_letter = move_letter(letter=i, moves=moves)
        output.append(moved_letter)
    return "".join(output)


def main():
    """Run sample move functions. Do not import."""
    print(move('hello'))
    print(move('Python'))
    print(move('PrOgrAms'))
    print(move('bye'))
    print(move('welcome'))
    print(move('Zebra'))


if __name__ == "__main__":
    main()
