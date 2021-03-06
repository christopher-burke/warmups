#!/usr/bin/env python3

"""Baseball stat formulas.

Collection of baseball formulas used for statistical analysis.
"""

from fractions import Fraction


def innings(innings: str):
    """Convert the partial innings pitched (outs) to a fraction.

    Baseball represents the thirds of innings in the following:
        * 0.1 = 1 of the 3 outs made, meaning 1/3.
        * 0.2 = 2 of the 3 outs made, meaning 2/3.

    These fractions need to be converted properly in order to be processed.
    """
    try:
        innings, fraction = innings.split('.')
        fraction = Fraction(int(fraction), 3)
        return int(innings) + fraction
    except ValueError:
        return int(innings)


def era(innings_pitched: float, er: int, total_innings: int=9) -> float:
    """Calculate a baseball pitcher's ERA.

    ERA = ('earned runs' / 'innings pitched') * 'total innings'

    er = Earned Runs

    """
    ERA = (er * total_innings) / innings(str(innings_pitched))
    return round(float(ERA), 2)


def whip(innings_pitched: float, bb: int, h: int) -> float:
    """Calculate a baseball pitcher's WHIP.

    WHIP = (BB + H) / IP

    bb = Walks / Base on balls
    h = hits

    """
    WHIP = (bb + h) / innings(str(innings_pitched))
    return round(float(WHIP), 2)


def main():
    """Run era and whip samples."""
    print(era(innings_pitched=6.0, er=3))
    print(era(innings_pitched=6.2, er=3))
    print(era(innings_pitched=154.1, er=52))

    print(whip(innings_pitched=202.1, bb=43, h=190))
    print(whip(innings_pitched=140.0, bb=38, h=130))
    print(whip(innings_pitched=154.1, bb=38, h=148))


if __name__ == "__main__":
    main()
