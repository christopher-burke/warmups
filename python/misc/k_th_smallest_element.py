#!/usr/bin/env python3

"""K’th Smallest/Largest Element in Unsorted Array.

This function returns k'th smallest element in array
using QuickSort based method.  

All elements in array are distinct.
"""
from pprint import pprint


def partition(array, left, right):

    pivot = array[right]
    i = left
    for j in range(left, right):
        if (array[j] <= pivot):
            temp_i = array[i]
            temp_j = array[j]
            array[j] = temp_i
            array[i] = temp_j
            i += 1
    temp_i = array[i]
    temp_right = array[right]
    array[right] = temp_i
    array[i] = temp_right
    print(array, i)
    return i


def find_element_postion(array, k):

    k = k - 1  # 0 indexed
    n = len(array) - 1
    pos = partition(array, 0, n)

    if (pos == k):
        return pos
    elif (pos > k):
        return find_element_postion(array[0:pos-1], k-len(array[pos:]))
    else:
        return find_element_postion(array[pos:n], k)


def main(array, k):
    pos = find_element_postion(array, k)
    print(f'Returned: {pos}')
    return array[pos]


if __name__ == "__main__":
    print(main(array=[7, 10, 4, 3, 20, 15, ], k=3))
    print('---')
    print('---')
    print('---')
    print(main(array=[7, 10, 4, 3, 20,  22, 15, 11, ], k=5))
    print(main(array=[7, 10, 4, 20, 15, ], k=4))
    print('---')
    print(sorted([7, 10, 4, 3, 20, 15, ])[2])
    print(sorted([7, 10, 4, 3, 20,  22, 15, 11, ])[4])
    print(sorted([7, 10, 4, 20, 15, ])[3])
