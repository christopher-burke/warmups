#!/usr/bin/env python3

"""Maximum sum increasing subsequence.

Given an array A of N positive integers. Find the sum of maximum
sum increasing subsequence of the given array.
"""


def max_sum_subsequence(A):
    """Find the maximum sum increasing subsequence."""
    increasing_subsequences = []
    for i, item in enumerate(A):
        remaining_sequence = A[i+1:]
        subsequence_ = [item]
        for j in remaining_sequence:
            if j > subsequence_[-1]:
                subsequence_.append(j)
            else:
                increasing_subsequences.append(tuple(subsequence_))
                if j > item:
                    subsequence_ = [item, j]
                else:
                    subsequence_ = [item]
        increasing_subsequences.append(tuple(subsequence_))
    max_sum = 0
    for x in set(increasing_subsequences):
        test_max_sum = sum(x)
        max_sum = test_max_sum if test_max_sum > max_sum else max_sum
    return max_sum


if __name__ == "__main__":
    print(max_sum_subsequence(A=(1, 101, 2, 3, 100, 4, 5)))
    print(max_sum_subsequence(A=(10, 5, 4, 3)))
    print(max_sum_subsequence(A=(10, 5, 4, 3, 15)))
