#!/usr/bin/env python3

"""Split Item Codes.

You have a list of item codes with the following format: "[letters][digits]"

Create a function that splits these strings into
their alphabetic and numeric parts.

Source:
https://edabit.com/challenge/CvChvza6kwweMjNRr
"""

import re


ALPHABETIC_NUMERIC = r'([A-Z, a-z]+)([0-9]+)'


def split_code(code: str) -> list:
    """Split code string to list [alphabetic, numeric]."""
    split_code_ = re.compile(ALPHABETIC_NUMERIC)
    match = split_code_.match(code)
    return [match.group(1), int(match.group(2)), ]


def split_code_mix(code: str) -> list:
    """Split code string to list, regardless of position."""
    code_lst = list(code)
    alpha = "".join([i for i in code_lst if i.isalpha()])
    numeric = int(("".join([i for i in code_lst if i.isnumeric()])))
    return [alpha, numeric, ]


def main():
    """Run sample split_code functions. Do not import."""
    assert split_code("TEWA8392") == ["TEWA", 8392]
    assert split_code("MMU778") == ["MMU", 778]
    assert split_code("SRPE5532") == ["SRPE", 5532]
    assert split_code("SKU8977") == ["SKU", 8977]
    assert split_code("MCI5589") == ["MCI", 5589]
    assert split_code("WIEB3921") == ["WIEB", 3921]
    print("Passed.")


if __name__ == "__main__":
    main()
