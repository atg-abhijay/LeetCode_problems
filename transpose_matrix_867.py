"""
URL of problem:
https://leetcode.com/problems/transpose-matrix/description/
"""


def main(A):
    A_rows = len(A)
    A_cols = len(A[0])
    B = [[0 for x in range(A_rows)] for x in range(A_cols)]

    for i in range(A_rows):
        row = A[i]
        for j in range(A_cols):
            elem = row[j]
            B[j][i] = elem

    print(B)
    # return B


if __name__ == '__main__':
    main([[1, 2, 3], [4, 5, 6]])
