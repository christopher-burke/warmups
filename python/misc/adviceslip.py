#!/usr/bin/env python3

"""Advice Slip - Random.

Using the adviceslip.com API (https://api.adviceslip.com/advice), get
a random advice slip and print it to the terminal.
"""

import json
from contextlib import closing
from urllib.request import urlopen


ADVICESLIP_URL = "https://api.adviceslip.com/advice"


def random_adviceslip() -> str:
    """Get random adviceslip."""
    action = closing(urlopen(ADVICESLIP_URL))
    with action as response:
        output = response.read().decode('utf-8')
    return output


def parse_advice(json_response) -> str:
    """Get the advice from the JSON response."""
    json_slip = json.loads(json_response)
    advice = json_slip['slip']['advice']
    return advice


def get_advice():
    """Get advice from adviceslip.com."""
    json_response = random_adviceslip()
    advice = parse_advice(json_response=json_response)
    return advice


def main():
    """Run get_advice function. Main Method do not import."""
    print(get_advice())


if __name__ == "__main__":
    main()
