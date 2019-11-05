#!/usr/bin/env python3

"""Smooth Sentences.

Carlos is a huge fan of something he calls smooth sentences.
A smooth sentence is one where the last letter of each word is identical
to the first letter the following word.

To illustrate, the following would be a smooth sentence:
"Carlos swam masterfully."

Since "Carlos" ends with an "s" and swam begins with an "s"
and swam ends with an "m" and masterfully begins with an "m".

Source:
https://edabit.com/challenge/veFgC7QFEBmG6xE3G
"""

import re


def is_smooth(sentence: str) -> bool:
    """Determine if the sentence is smooth."""
    spaces = re.findall(r'\w\s\w', sentence)
    check = [len(set(match.lower().split(' '))) for match in spaces]
    return len(check) == sum(check)


def main():
    """Run sample is_smooth functions."""
    assert is_smooth("Carlos swam masterfully.") is True
    assert is_smooth(
        "Marta appreciated deep perpendicular right trapezoids") is True
    assert is_smooth("Someone is outside the doorway") is False
    assert is_smooth("She eats super righteously") is True
    assert is_smooth("Ben naps so often") is True
    assert is_smooth("Cute triangles are cute") is False
    assert is_smooth("Mad dislikes sharp pointy yoyos") is True
    assert is_smooth("Rita asks Sam mean numbered dilemmas") is True
    assert is_smooth("Marigold daffodils streaming happily.") is False
    assert is_smooth("Simply wonderful laughing.") is False
    print('Passed.')


if __name__ == "__main__":
    main()
