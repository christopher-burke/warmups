#!/usr/bin/env python3

"""Stock buy and sell.

The cost of stock on each day is given in an array A.
Find all the days on which you buy and sell the stock so that in between
those days your profit is maximum.

Source:
https://practice.geeksforgeeks.org/problems/stock-buy-and-sell/0

"""


def maximum_profit(stock_prices: list) -> str:
    """Determine the max profit."""
    # Setup
    results = []
    days = len(stock_prices)
    if days == 1:
        return
    count = 0
    index = 0

    # Logic
    while (index < days - 1):
        while ((index < days-1) and
                (stock_prices[index+1] <= stock_prices[index])):
            index += 1

        if (index == days-1):
            break

        index += 1
        buy = index

        while ((index < days) and
                (stock_prices[index] >= stock_prices[index-1])):
            index += 1

        sell = index-1

        results.append((buy-1, sell,))

        count += 1

    # Return statements.
    if count:
        return " ".join([str(i) for i in results])
    return "No Profit."


def main():
    list(map(print,
             [
                 maximum_profit(
                     stock_prices=[100, 180, 260, 310, 40, 535, 695, ]
                 ),
                 maximum_profit(
                     stock_prices=[23, 13, 25, 29, 33, 19, 34, 45, 65, 67, ]
                 ),
                 maximum_profit(
                     stock_prices=[1, 1, 1, 1, 1, ]
                 ),
             ]
             )
         )


if __name__ == "__main__":

    main()
