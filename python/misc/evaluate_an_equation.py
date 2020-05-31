#!/usr/bin/env python3

"""Evaluate an Equation.

Create a function that evaluates an equation.

Source:
https://edabit.com/challenge/QM6ZgHxvQCDX9Tzoa
"""


def eq(equation: str) -> int:
    """Evaluate the equation."""
    code = compile(equation, "<string>", "eval")
    return eval(code)

def main():
    """Run sample functions. Do not import."""
    assert eq("1+2") == 3
    assert eq("6/(9-7)") == 3
    assert eq("3+2-4") == 1
    assert eq("3*4+1") == 13
    assert eq("5*8-4*9") == 4
    assert eq("3**7") == 2187
    assert eq("(6**3)+3") == 219
    print('Passed.')

if __name__ == "__main__":
    main()