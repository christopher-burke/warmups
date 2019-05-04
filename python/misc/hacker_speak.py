#!/usr/bin/env python3

"""Hacker Speak - H4ck3r Sp34k.

Create a function that takes a string as an argument
and returns a coded (h4ck3r 5p34k) version of the string.

Mapping:
* a->4
* e->3
* i->1
* o->0
* s->5

Source:
https://edabit.com/challenge/nPdPSgSsGfdyRbHkd
"""


hacker_speak_mapping = {'a': '4',
                        'e': '3',
                        'i': '1',
                        'o': '0',
                        's': '5',
                        }


def hacker_speak(text: str) -> str:
    """Convert text to hacker speak."""
    hacker_speak_ = \
        ''.join([hacker_speak_mapping.get(char.lower(), char)
                 for char in text])
    return hacker_speak_


def main():
    """Run sample hacker_speak functions. Do not import."""
    print(hacker_speak("javascript is cool"))  # "j4v45cr1pt 15 c00l"
    print(hacker_speak("programming is fun"))  # "pr0gr4mm1ng 15 fun"
    print(hacker_speak("become a coder"))  # "b3c0m3 4 c0d3r"


if __name__ == "__main__":
    main()
