#!/usr/bin/env python3

"""Drinks Allowed.

A bartender is writing a simple program to determine whether he should serve
drinks to someone. He only serves drinks to people 18 and older and when
he's not on break.

Given the person's age, and whether break time is in session, create a
function which returns whether he should serve drinks.

Source:
https://edabit.com/challenge/iipAZ7sK8C5sRF8K6
"""


def should_serve_drinks(age: int, on_break: bool) -> bool:
    """Serve drinks based on age and break."""
    return (age >= 18) and not(on_break)


def main():
    """Run sample functions. Do not import."""
    assert should_serve_drinks(17, True) == False
    assert should_serve_drinks(30, True) == False
    assert should_serve_drinks(24, False) == True
    assert should_serve_drinks(18, False) == True
    assert should_serve_drinks(3, False) == False
    print('Passed.')

if __name__ == "__main__":
    main()