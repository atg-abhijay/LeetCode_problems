"""
URL of problem:
https://leetcode.com/problems/transpose-matrix/description/
"""


def main(A):
    """
    main method for running the program.
    Argument:
        A - a nxm matrix
    Prints:
        B - Transpose of matrix A (dimension - mxn)
    """
    # number of rows
    # and columns in A
    A_rows = len(A)
    A_cols = len(A[0])
    # double list comprehension to initialize
    # transpose matrix to zero -
    # the first comprehension (on the left) makes a
    # list of zeroes, having length 'r' (#rows in A).
    # this gives us one row in the transpose matrix.
    # there are 'c' rows in it ('c': #columns in A).
    # repeat the r-length row c times to get the transpose.
    B = [[0 for x in range(A_rows)] for x in range(A_cols)]

    # for matrix A and its transpose
    # B, A[i][j] = B[j][i]
    for i in range(A_rows):
        row = A[i]
        for j in range(A_cols):
            elem = row[j]
            B[j][i] = elem

    print(B)
    # return B


if __name__ == '__main__':
    main([[1, 2, 3], [4, 5, 6]])
