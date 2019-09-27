#!/usr/bin/env python3

"""Unique Character Mapping

Write a function that returns a character mapping from a word.

Start your counter at 0, and increment by 1 each time you encounter
a new character.

Identical characters should share the same number.

Source:
https://edabit.com/challenge/yPsS82tug9a8CoLaP
"""

from collections import defaultdict


def character_mapping(text: str) -> list:
    """Find the character mapping of text."""
    start_index = 0
    character_map = defaultdict(lambda: start_index)
    result = []
    for character in text:
        if character in character_map.keys():
            result.append(character_map[character])
        else:
            result.append(character_map[character])
            start_index += 1
    return result


def main():
    """Run sample character_mapping functions. Do not import."""
    assert character_mapping("abcd") == [0, 1, 2, 3]
    assert character_mapping("abb") == [0, 1, 1]
    assert character_mapping("babbcb") == [0, 1, 0, 0, 2, 0]
    assert character_mapping("aaabb") == [0, 0, 0, 1, 1]
    assert character_mapping("abccbc") == [0, 1, 2, 2, 1, 2]
    assert character_mapping("fluffy") == [0, 1, 2, 0, 0, 3]
    assert character_mapping("madness") == [0, 1, 2, 3, 4, 5, 5]
    assert character_mapping("buttery") == [0, 1, 2, 2, 3, 4, 5]
    assert character_mapping("canine") == [0, 1, 2, 3, 2, 4]
    assert character_mapping("hohoho") == [0, 1, 0, 1, 0, 1]
    assert character_mapping("hmmmmm") == [0, 1, 1, 1, 1, 1]
    assert character_mapping("") == []
    print('Passed.')


if __name__ == "__main__":
    main()
