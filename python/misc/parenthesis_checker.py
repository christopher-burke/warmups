#!/usr/bin/env python3

"""Parenthesis Checker.

Given an expression string exp.
Examine whether the pairs and the orders of
“{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for
exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”
"""

from collections import namedtuple

pairs = namedtuple("Pairs", ["start", "end"])

search = {"{": pairs(start="{", end="}"),
          "(": pairs(start="(", end=")"),
          "[": pairs(start="[", end="]")
          }


def parenthesis_checker(exp):
    """Check the balance of parenthesis."""
    stack = ""  # Use string as a stack
    for i in exp:
        stack += i
        if len(stack) >= 2:
            try:
                test_case = search[stack[-2]].end
            except KeyError:
                break  # Seen an ending pair before a start pair
            if test_case == stack[-1]:

                stack = stack[0:-2]  # Match remove the pair from the stack
    if len(stack) > 0:
        return 'unbalanced'
    return 'balanced'


if __name__ == "__main__":
    print(parenthesis_checker('{([])}'))
    print(parenthesis_checker('()'))
    print(parenthesis_checker('({})]'))
    print(parenthesis_checker('({})]'))
    print(parenthesis_checker('(()})'))
    print(parenthesis_checker('}}}}}}'))
