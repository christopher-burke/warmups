#!/usr/bin/env python3

"""Anagram.

Given two strings, check whether two given
strings are anagram of each other or not.
An anagram of a string is another string
that contains same characters, only the
order of characters can be different.

For example, “act” and “tac” are
anagrams of each other.

Source: https://practice.geeksforgeeks.org/problems/anagram/0
"""


from collections import defaultdict


def letter_count(text):
    """Count the letters of text using defaultdict."""
    letter_count_dict = defaultdict(int)
    for letter in text:
        letter_count_dict[letter] += 1
    return letter_count_dict


def anagram(text: str, check: str) -> bool:
    """Determine if the text and check are anagrams."""
    if len(text) != len(check):
        return False
    else:
        text_dict = letter_count(text)
        check_dict = letter_count(check)
        is_anagram = text_dict == check_dict
        return is_anagram


def main(inputs: str):
    """Run anagram function as a main method."""
    text, check = inputs.split(" ")
    return anagram(text=text, check=check)


if __name__ == "__main__":
    print(main("geeksforgeeks forgeeksgeeks"))
    print(main("allergy allergic"))
