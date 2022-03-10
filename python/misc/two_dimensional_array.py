#!/usr/bin/env python3

"""Set columns and rows as zeros.

Given a two-dimensional array, if any element within is zero, make its whole row and column zero.
"""


two_dimensional_array = [[1, 1, 2, 3, ],
                         [1, 2, 3, 4, ],
                         [1, 0, 1, 1, ],
                         [1, 1, 1, 1, ],
                         [5, 5, 5, 0, ],
                         ]


def row_col_make_zero(two_dimensional_array):
    """Set columns and rows as zeros in a 2D array."""
    columns = []
    rows = []
    for row, rvalue in enumerate(two_dimensional_array):
        check = [column for column, cvalue in enumerate(rvalue) if cvalue == 0]
        if check:
            columns.extend(check)
            rows.append(row)
    for row in two_dimensional_array:
        for column in columns:
            row[column] = 0
    for row in rows:
        two_dimensional_array[row] = [0]*len(two_dimensional_array[row])
    print(two_dimensional_array)


if __name__ == "__main__":
    row_col_make_zero(two_dimensional_array=two_dimensional_array)
