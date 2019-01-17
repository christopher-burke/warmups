#!/usr/bin/env python3

"""Python Random Number Generation Exercises.

This random number generation exercise questions is to help
Python developer quickly learn the various techniques of how to generate
random numbers and data in Python.

This random number generation exercise and challenge
helps you to understand python random module, secrets module, and its methods.

I decided to answer each question as it's own class object.

Source:
https://pynative.com/python-random-number-generation-exercise-questions-and-challenge/
"""


import random


class QuestionOne:
    """QuestionOne Class."""

    def __init__(self, *args, **kwargs):
        """Create QuestionOne object."""
        self.number = 1
        self.title = "Generate 3 random integers between 100 and 999 which"\
            " is divisible by 5"
        self.question = "Question 1: Generate 3 random integers between"\
            "100 and 999 which is divisible by 5"
        self.solution = self.solve()

    def solve(self, print_=False):
        """Find a solution for the question."""
        print(f"## Question {self.number} ##")
        print(f"* {self.question}")
        print("Solution:  \n[random.randrange(100, 999, 5) for i in range(3)]")
        return [random.randrange(100, 999, 5)
                for i in range(3)]


class QuestionTwo:
    """QuestionTwo Class."""

    def __init__(self, *args, **kwargs):
        """Create QuestionTwo object."""
        self.number = 2
        self.title = "Random Lottery Pick."
        self.question = "".join(
            ["Lottery game –  Generate a 100 Lottery tickets and",
             " pick two lucky tickets from it as a winner.",
             ]
        )
        self.solution = self.solve()

    def solve(self):
        """Find a solution for the question."""
        print(f"## Question {self.number} ##")
        print(f"* {self.question}")
        print("".join([
            "Solution:  \n",
            "lottery_tickets= [random.randrange(",
            "1000000000, 9999999999) for _ in range(100)]",
            "winning_tickets= random.sample(lottery_tickets, 2)",
        ]))
        lottery_tickets = [random.randrange(
            1000000000, 9999999999) for _ in range(100)]
        winning_tickets = random.sample(lottery_tickets, 2)
        return winning_tickets


def main():
    """Run all Question Solutions."""
    print(QuestionOne().solution)
    print(QuestionTwo().solution)


if __name__ == "__main__":
    main()
