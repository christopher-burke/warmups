#!/usr/bin/env python3

"""International Greetings.

Suppose you have a guest list of students and the country they are from, stored as key-value pairs in a dictionary.

GUEST_LIST = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}

Write a function that takes in a name and returns a name tag, that should read:

    "Hi! I'm [name], and I'm from [country]."

If the name is not in the dictionary, return:

    "Hi! I'm a guest."


Source:
https://edabit.com/challenge/vAS4Hp4wzSEnQs3tZ
"""
GUEST_LIST = {
    "Randy": "Germany",
    "Karla": "France",
    "Wendy": "Japan",
    "Norman": "England",
    "Sam": "Argentina"
}


def greeting(name: str) -> str:
    """Greet the user from the guest list."""
    country = GUEST_LIST.get(name, None)
    if country:
        return f"Hi! I'm {name}, and I'm from {country}."
    return "Hi! I'm a guest."


def main():
    """Run sample greetings functions. Do not import."""
    assert greeting("Randy") == "Hi! I'm Randy, and I'm from Germany."
    assert greeting("Sam") == "Hi! I'm Sam, and I'm from Argentina."
    assert greeting("Monti") == "Hi! I'm a guest."
    assert greeting("Trudy") == "Hi! I'm a guest."
    assert greeting("Wendy") == "Hi! I'm Wendy, and I'm from Japan."
    print('Passed.')


if __name__ == "__main__":
    main()
