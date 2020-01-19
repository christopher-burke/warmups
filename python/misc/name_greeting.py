#!/usr/bin/env python3

"""Name Greeting!

Create a function that takes a name and returns a greeting.

Source:
https://edabit.com/challenge/coRuMC4Ykksti8Z47
"""


def hello_name(name: str):
    """Return a string greeting the name."""
    return f"Hello {name}!"


def main():
    """Run sample hello_name functions. Do not import."""
    assert hello_name("Gerald") == "Hello Gerald!"
    assert hello_name("Fatima") == "Hello Fatima!"
    assert hello_name("Ed") == "Hello Ed!"
    assert hello_name("Tiffany") == "Hello Tiffany!"
    print('Passed.')


if __name__ == "__main__":
    main()
