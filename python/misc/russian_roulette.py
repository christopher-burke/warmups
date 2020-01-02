#!/usr/bin/env python3

"""Russian roulette."""

import random

RESULTS = {
    "click": True,  # True value represents Survived.
    "bang": False,  # False value represents Failure.
}


class Revolver:
    def __init__(self, chambers=6, bullet=1):
        if bullet > chambers:
            raise ValueError(
                f"Number of bullet is greater than chambers. chambers= {chambers}, bullet= {bullet}")
        empty_chambers = chambers - bullet
        loaded_chamber = random.randint(0, empty_chambers)
        self.shots = 0
        self.chamber = tuple(
            "bang" if i == loaded_chamber else "click"
            for i in range(chambers))

    def __iter__(self):
        return self

    def __next__(self):
        for shot in self.chamber[self.shots:]:
            result = shot
            self.shots += 1
            return result
        raise StopIteration


def russian_roulette_gen(chambers=6, bullet=1):
    """Russian Roulette Generator function."""
    empty_chambers = chambers - bullet
    loaded_chamber = random.randint(0, empty_chambers)
    chamber = tuple(
        "bang" if i == loaded_chamber else "click"
        for i in range(chambers))
    for shot in chamber:
        yield shot


def main():
    """Play Russian Roulette."""
    revolver = Revolver()
    result = next(revolver)
    return result


if __name__ == "__main__":
    print(RESULTS.get(main()))
