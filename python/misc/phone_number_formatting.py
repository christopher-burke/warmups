#!/usr/bin/env python3

"""Phone Number Formatting.

Create a function that takes a list of 10 numbers (between 0 and 9)
and returns a string of those numbers formatted as a phone number 
(e.g. (555) 555-5555).

Source:
https://edabit.com/challenge/bPHcgMpkf9WvbwbAo
"""


def phone_number_format(iterable: list) -> str:
    """Format a list of integers into a phone number."""
    if not len(iterable) == 10:
        raise ValueError('Phone numbers need 10 digits.')

    return_string = "".join([str(i) for i in iterable])
    area_code = f"({return_string[0:3]})"
    phone_number = f"{return_string[3:6]}-{return_string[6:]}"

    return f"{area_code} {phone_number}"


def main():
    """Main method. Do not import."""
    print(phone_number_format([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    print(phone_number_format([5, 1, 9, 5, 5, 5, 4, 4, 6, 8]))
    print(phone_number_format([3, 4, 5, 5, 0, 1, 2, 5, 2, 7]))


if __name__ == "__main__":
    main()
