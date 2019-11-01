#!/usr/bin/env python3

"""Words With Duplicate Letters.

Given a common phrase, return False if any individual word in the phrase
contains duplicate letters. Return True otherwise.

Source:
https://edabit.com/challenge/WS6hR6b9EZzuDTD26
"""


def no_duplicate_letters(phrase: str) -> bool:
    """Check if each word has distinct letters in phrase."""
    words = phrase.split(' ')
    for word in words:
        if len(set(word)) == len(word):
            continue
        else:
            return False
    return True


def main():
    """Run sample no_duplicate_letters functions. Do not import."""
    assert no_duplicate_letters("Easy does it.") is True
    assert no_duplicate_letters("So far, so good.") is False
    assert no_duplicate_letters("Better late than never.") is False
    assert no_duplicate_letters("Beat around the bush.") is True
    assert no_duplicate_letters(
        "Give them the benefit of the doubt.") is False
    assert no_duplicate_letters(
        "Your guess is as good as mine.") is False
    assert no_duplicate_letters("Make a long story short.") is True
    assert no_duplicate_letters("Go back to the drawing board.") is True
    assert no_duplicate_letters(
        "Wrap your head around something.") is True
    assert no_duplicate_letters("Get your act together.") is False
    assert no_duplicate_letters("To make matters worse.") is False
    assert no_duplicate_letters("No pain, no gain.") is True
    assert no_duplicate_letters(
        "We'll cross that bridge when we come to it.") is False
    assert no_duplicate_letters("Call it a day.") is False
    assert no_duplicate_letters("It's not rocket science.") is False
    assert no_duplicate_letters("A blessing in disguise.") is False
    assert no_duplicate_letters("Get out of hand.") is True
    assert no_duplicate_letters("A dime a dozen.") is True
    assert no_duplicate_letters(
        "Time flies when you're having fun.") is True
    assert no_duplicate_letters("The best of both worlds.") is True
    assert no_duplicate_letters("Speak of the devil.") is True
    assert no_duplicate_letters("You can say that again.") is False
    print('Passed.')


if __name__ == "__main__":
    main()
