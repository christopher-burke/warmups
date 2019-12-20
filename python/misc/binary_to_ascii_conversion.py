#!/usr/bin/env python3

"""Binary to ASCII Conversion.

Create a function that takes a string of 1's and 0's (binary) as an argument
and return the equivalent decoded ASCII text. Characters can be in the range of
"00000000" to "11111111", which means every eight digits of binary input
represents a single character.

a = 01100001
b = 01100010
c = 01100011

If you were to combine these characters into the string "abc", the
corresponding binary would be 011000010110001001100011.

Source:
https://edabit.com/challenge/Wm8Zin8gQGsupNmbJ
"""


import re


def binary_conversion(txt):
    """Convert binary txt to ascii string."""
    if len(txt) % 8 > 0:
        raise ValueError(f"txt length is not base 8. The value of txt:  {txt}")
    ascii_message = "".join([chr(int(byte, 2))
                             for byte in re.findall(r"\d{8}", txt)]
                            )
    return ascii_message


def main():
    """Run sample binary_conversion functions. Do not import."""
    assert binary_conversion(
        "011001010110010001100001011000100110100101110100") == 'edabit'
    assert binary_conversion("001100010011001000110011") == "123"
    assert binary_conversion(
        "010010000110010101101100011011000110111100111111") == "Hello?"
    assert binary_conversion("") == ""
    assert binary_conversion("0010000101000000001000110010010000100101010111100010011000101010001010000010100101010001010101110100010101110010011101000111100101010101010010010100111101001100011001000110011001100111011000100110001001101000011011100110110101001001010010110100001001001010010010110100100001001001010101010100111100101000001111110011111000111111001111000111111001111110011111100111111001111110001010010010100000101010001001100010010101011110001110010011100000110111001100010011001100101111001011010010111100101010001011010010101000101111") == "!@#$%^&*()QWErtyUIOLdfgbbhnmIKBJKHIUO(?>?<~~~~~)(*&%^98713/-/*-*/"
    print('Passed.')


if __name__ == "__main__":
    main()
