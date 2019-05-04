#!/usr/bin/env python3

"""ATM PIN Code Validation.

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain
anything but exactly 4 digits or exactly 6 digits. Your task is to
create a function that takes a string and returns True if the PIN
is valid and False if it's not.

Source:
https://edabit.com/challenge/K4Pqh67Y9gpixPfjo
"""


def is_valid_pin(pin: str) -> bool:
    """Determine if pin is valid ATM pin."""
    if len(pin) in (4, 6):
        try:
            return bool([int(i) for i in pin])
        except ValueError:
            return False
    return False


def main():
    """Run sample is_valid_pin function."""
    print(is_valid_pin("1234"))
    print(is_valid_pin("12345"))
    print(is_valid_pin("a234"))
    print(is_valid_pin(""))


if __name__ == "__main__":
    main()
