#!/usr/bin/env python3

"""Profitable Gamble.

Create a function that takes in 3 parameters (probability of winning,
prize value, and cost of playing) and returns whether or not
the gamble is profitable.

A profitable gamble is a game that yields a positive net profit,
where net profit is calculated in the following manner:
net_outcome = probability_of_winning * prize - cost_of_playing.

Source:
https://edabit.com/challenge/SNM5EZ3FePECt2HQn

"""

from decimal import Decimal


def profitable_gamble(probability_of_winning, prize, cost) -> bool:
    """Determine if the gamble is profitable.

    Gambles are profitable if the net profit is positive.

    Arguments:
        probability_of_winning {Decimal} -- Winning Probability.
        prize {Decimal} -- Winning value.
        cost {Decimal} -- Cost of playing the game.

    Returns:
        bool -- [description]

    """
    probability_of_winning = Decimal(probability_of_winning)
    prize = Decimal(prize)
    cost = Decimal(cost)
    net_outcome = (probability_of_winning * prize) - cost
    profitable = net_outcome > 0
    return profitable


def main():
    """Run sample profitable_gamble."""
    print(profitable_gamble(0.2, 50, 9))
    print(profitable_gamble(0.9, 1, 2))
    print(profitable_gamble(0.9, 3, 2))


if __name__ == "__main__":
    main()
