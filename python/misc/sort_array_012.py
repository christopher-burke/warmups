#!/usr/bin/env python3

"""Sort an array of 0s, 1s and 2s


Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.

Input:
The first line contains an integer 'T' denoting the total number of test cases. Then T testcases follow. Each testcases contains two lines of input. The first line denotes the size of the array N. The second lines contains the elements of the array A separated by spaces.

Output: 
For each testcase, print the sorted array.

Constraints: 
1 <= T <= 500
1 <= N <= 106
0 <= Ai <= 2

Example:
Input :
2
5
0 2 1 2 0
3
0 1 0

Output:
0 0 1 2 2
0 0 1
"""


def sort_array_012(array):
    """Sort an array of 0s, 1s and 2s."""
    # Dictionary of numbers encountered
    data = {0: 0, 1: 0, 2: 0}
    output = ''
    for x in array:
        data[x] = data[x] + 1

    for key, value in data.items():
        output += f'{key},' * value

    return output.split(',')[:-1]


if __name__ == "__main__":
    print(sort_array_012([0, 2, 1, 2, 0, ]))
    print(sort_array_012([0, 1, 0, ]))
