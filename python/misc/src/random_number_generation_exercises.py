#!/usr/bin/env python3

"""Python Random Number Generation Exercises.

This random number generation exercise questions is to help
Python developer quickly learn the various techniques of how to generate
random numbers and data in Python.

This random number generation exercise and challenge
helps you to understand python random module, secrets module, and its methods.

I decided to answer each question as it's own class object.

Source: https://pynative.com/python-random-number-generation-exercise-questions-and-challenge/
"""


import random


class QuestionOne:

    def __init__(self, *args, **kwargs):
        self.number = 1
        self.question = "Question 1: Generate 3 random integers between"\
            "100 and 999 which is divisible by 5"
        self.solution = self.solve()

    def solve(self):
        """Find a solution for the question."""
        return [random.randrange(100, 999, 5)
                for i in range(3)]


def main():
    print(QuestionOne().solution)


if __name__ == "__main__":
    main()
