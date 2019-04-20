#!/usr/bin/env python3

"""Maskify the String.

Usually when you sign up for an account to buy something,
your credit card number, phone number or answer to a secret
question is partially obscured in some way. Since someone could
look over your shoulder, you don't want that shown on your screen.
Hence, the website masks these strings.

Your task is to create a function that takes a string,
transforms all but the last four characters into "#"
and returns the new masked string.

Source:
https://edabit.com/challenge/xRzyWsdzMEeGqsJMK
"""


def maskify(account_id: str) -> str:
    """Create a masked string."""
    if account_id == '':
        return account_id

    if len(account_id) > 4:
        return '#' * (len(account_id) - 4) + account_id[-4:]
    return account_id


def main():
    """Run sample maskify functions. Do not import."""
    print(maskify("4556364607935616"))  # ➞ "############5616"
    print(maskify("64607935616"))  # ➞ "#######5616"
    print(maskify("1"))  # ➞ "1"
    print(maskify(""))  # ➞ ""


if __name__ == "__main__":
    main()
