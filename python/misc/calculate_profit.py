#!/usr/bin/env python3

"""Calculate the Profit.

You work for a manufacturer, and have been asked to calculate the total
profit made on the sales of a product. You are given a dictionary containing
the cost price per unit (in dollars), sell price per unit (in dollars),
and the starting inventory. Return the total profit made, rounded to the
nearest dollar. Assume all of the inventory has been sold.

Source:
https://edabit.com/challenge/YfoKQWNeYETb9PYpw
"""

from typing import Dict


def profit(info: Dict) -> int:
    """Calculate the profit from info."""
    profit_ = (info['sell_price'] - info['cost_price']) * info['inventory']
    return round(profit_)


def main():
    """Run sample profit functions. Do not import."""
    assert profit({'cost_price': 32.67, 'sell_price': 45.00,
                   'inventory': 1200}) == 14796
    assert profit({'cost_price': 0.1, 'sell_price': 0.18,
                   'inventory': 259800}) == 20784
    assert profit({'cost_price': 185.00, 'sell_price': 299.99,
                   'inventory': 300}) == 34497
    assert profit({'cost_price': 378.11, 'sell_price': 990.00,
                   'inventory': 99}) == 60577
    assert profit({'cost_price': 4.67, 'sell_price': 5.00,
                   'inventory': 78000}) == 25740
    assert profit({'cost_price': 19.87, 'sell_price': 110.00,
                   'inventory': 350}) == 31546
    assert profit({'cost_price': 2.91, 'sell_price': 4.50,
                   'inventory': 6000}) == 9540
    assert profit({'cost_price': 68.01, 'sell_price': 149.99,
                   'inventory': 500}) == 40990
    assert profit({'cost_price': 1.45, 'sell_price': 8.50,
                   'inventory': 10000}) == 70500
    assert profit({'cost_price': 10780, 'sell_price': 34999,
                   'inventory': 10}) == 242190
    print('Passed.')


if __name__ == "__main__":
    main()
