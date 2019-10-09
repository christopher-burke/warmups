#!/usr/bin/env python3

"""Fewest bills and coins."""

from collections import namedtuple

Money = namedtuple('Money', "value name")


BILLS = (
    Money(100, "hundred dollar bill"),
    Money(50, "fifty dollar bill"),
    Money(20, "twenty dollar bill"),
    Money(10, "ten dollar bill"),
    Money(5, "five dollar bill"),
    Money(1, "one dollar bill"),
)
COINS = (
    Money(25, "quarter"),
    Money(10, "dime"),
    Money(5, "nickel"),
    Money(1, "penny"),
)


def determine_fewest(value, denominations):
    """Find the fewest denominations needed."""
    fewest = []
    total_value = int(value)
    while total_value > 0:
        for denomination in denominations:
            if denomination.value > total_value:
                continue
            number_ = total_value//denomination.value
            fewest.append((number_, denomination,))
            total_value = total_value - (denomination.value * number_)
    return fewest


def in_words(fewest):
    """"""
    words = "\n".join(
        [f"{amount[0]} {amount[1].name}{'s' if amount[0] >1 else ''}"
         for amount in fewest])
    words = words.replace('pennys', 'pennies')
    words = f"{words}\n" if words else f"{words}"
    return words


def fewest_bills_coins(value) -> list:
    """Determine the fewest bills and coins for the value."""
    bills, _, coins = str(value).partition(".")
    coins = f"{coins}0" if len(coins) == 1 else coins

    fewest_bills = determine_fewest(bills, BILLS)
    fewest_coins = determine_fewest(coins, COINS)

    fewest_bills_in_words = in_words(fewest_bills)
    fewest_coins_in_words = in_words(fewest_coins)

    return f"{fewest_bills_in_words}{fewest_coins_in_words}"


def main():
    """Run sample fewest_bills_coins functions. Do not import."""
    assert fewest_bills_coins(
        101.01) == "1 hundred dollar bill\n1 one dollar bill\n1 penny\n"
    assert fewest_bills_coins(
        218.10) == "2 hundred dollar bills\n1 ten dollar bill\n1 five dollar bill\n3 one dollar bills\n1 dime\n"
    assert fewest_bills_coins(00.05) == "1 nickel\n"
    assert fewest_bills_coins(00.20) == "2 dimes\n"
    assert fewest_bills_coins(
        15.20) == "1 ten dollar bill\n1 five dollar bill\n2 dimes\n"
    assert fewest_bills_coins(
        20.21) == "1 twenty dollar bill\n2 dimes\n1 penny\n"
    assert fewest_bills_coins(
        49.17) == "2 twenty dollar bills\n1 five dollar bill\n4 one dollar bills\n1 dime\n1 nickel\n2 pennies\n"
    assert fewest_bills_coins(50.00) == "1 fifty dollar bill\n"
    assert fewest_bills_coins(
        47.63) == "2 twenty dollar bills\n1 five dollar bill\n2 one dollar bills\n2 quarters\n1 dime\n3 pennies\n"
    assert fewest_bills_coins(
        787.93) == "7 hundred dollar bills\n1 fifty dollar bill\n1 twenty dollar bill\n1 ten dollar bill\n1 five dollar bill\n2 one dollar bills\n3 quarters\n1 dime\n1 nickel\n3 pennies\n"
    print('Passed.')


if __name__ == "__main__":
    main()
