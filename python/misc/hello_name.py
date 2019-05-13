#!/usr/bin/env python3

"""Hello name.

Basic example of getting input from user and displaying a message.

Uses Python f-strings and builtins `input` and `print`.
"""


def say_hello(name: str, salutation: str = "Hello") -> str:
    """Say hello to the user."""
    return f"{salutation.capitalize()}, {name.capitalize()}. Welcome to the wonderful world of Python."


def ask_name(question: str = "What is your name?") -> str:
    """Ask for the users name."""
    return input(question)


def main():
    """Ask for name and say hello. Do Not Import."""
    name = ask_name()
    print(say_hello(name=name))


if __name__ == "__main__":
    main()
