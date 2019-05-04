#!/usr/bin/env python3

"""Missing number in array

Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case first line contains N(size of array). The subsequent line contains N-1 array elements.

Output:
Print the missing number in array.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ C[i] ≤ 107

Example:
Input:
2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10

Output:
4
9

Explanation:
Testcase 1: Given array : 1 2 3 5. Missing element is 4
"""


def find_missing_number(C, size: int) -> int:
    """Find the missing number.

    Find the missing number using the
    difference between sum of known and
    arithmetic sums.
    """
    known_numbers_sum = sum(C)
    expected_numbers_sum = (size/2) * (C[0] + C[-1])

    return int(expected_numbers_sum - known_numbers_sum)


if __name__ == "__main__":
    print(find_missing_number([1, 2, 3, 5], 5))
    print(find_missing_number([1, 2, 3, 4, 5, 6, 7, 8, 10], 10))
    print(find_missing_number([3, 4, 5, 6, 7, 8, 10], 8))
