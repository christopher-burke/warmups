#!/usr/bin/env python3

"""Number of Ways to Decode an encoded string.

A message containing letters from A-Z is being encoded to numbers using the following mapping:  
'A' -> 1,'B' -> 2...'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

### Example 1: ###
Input: "12
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

### Example 2: ###
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6). 
"""


def decode(number: str) -> bool:
    """Return if number is valid."""
    if int(number) > 0 and int(number) < 27:
        return True
    return False


def total_number_messages_decoded(message: str) -> int:
    """Return the total number of messages."""
    output_count = 1
    for index in range(len(message)):
        if index + 1 >= len(message):
            return output_count
        if message[index] != '0':
            possible_char = str(message[index] + str(message[index+1]))
            if decode(possible_char):
                output_count += 1
    return output_count


def main():
    """Run examples."""
    print(total_number_messages_decoded("12"))
    print(total_number_messages_decoded("226"))


if __name__ == "__main__":
    main()
