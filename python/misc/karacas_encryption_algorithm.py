#!/usr/bin/env python3

"""The Karaca's Encryption Algorithm.

Make a function that encrypts a given input with these steps:

1. Reverse the input.
2. Replace all vowels using the following chart:
    a => 0
    e => 1
    o => 2
    u => 3
3. Add "aca" to the end of the word/

Source:
https://edabit.com/challenge/JzBLDzrcGCzDjkk5n
"""


def encrypt(text: str) -> str:
    """Encrypt the text using Karaca's Encryption Algorithm."""
    encrypt_text = text[::-1]
    translation = encrypt_text.maketrans("aeou", "0123")
    return f"{encrypt_text.translate(translation)}aca"


def main():
    """Run sample encrypt functions, Do not import."""
    assert encrypt("banana") == "0n0n0baca"
    assert encrypt("karaca") == "0c0r0kaca"
    assert encrypt("burak") == "k0r3baca"
    assert encrypt("alpaca") == "0c0pl0aca"
    assert encrypt("hello") == "2ll1haca"
    print("Passed.")


if __name__ == "__main__":
    main()
