#!/usr/bin/env python3

"""Merge Sort Example.

Given an array A on size N, you need to find the number of ordered pairs  such that and .

Input:
First line contains one integer, N, size of array.
Second line contains N space separated integers denoting the elements of the array A.

Output:
Print the number of ordered pairs  such that and .

Constraints:

1 <= N <= 10**6
1 <= A[i] <= 10**6

SAMPLE INPUT
5
1 4 3 2 5

SAMPLE OUTPUT
3
"""


A = [1, 4, 3, 2, 5]
N = 5


def merge(A, start, mid, end):
    p = start
    q = mid+1
    Arr = []
    k = 0

    for i in range(end):
        if p > mid:
            k += 1
            q += 1
            Arr[k] = A[q]
        elif q > end:
            k += 1
            p += 1
            Arr[k] = A[p]
        elif A[p] < A[q]:
            k += 1
            p += 1
            Arr[k] = A[p]
        else:
            k += 1
            q += 1
            Arr[k] = A[q]

    A = Arr[:]
    return A


def merge_sort(A, start, end):
    if start < end:
        mid = (start + end)//2
        print(mid)
        merge_sort(A, start, mid)
        merge_sort(A, mid+1, end)

        return merge(A, start, mid, end)


def main(N, A):
    print(merge_sort(A, 0, N))


if __name__ == "__main__":
    main(A=[1, 4, 3, 2, 5, ], N=5)
