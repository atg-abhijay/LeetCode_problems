"""
URL of problem:
https://leetcode.com/problems/transpose-matrix/description/
"""


def main(A):
    A_rows = len(A)
    A_cols = len(A[0])

    # B = [0 for x in range(A_cols)[0 for x in range(A_rows)]]
    B = [[0 for x in range(A_rows)] for x in range(A_cols)]
    # print(B)
    # B_rows = A_cols
    # B_cols = A_rows

    # b_i = 0
    # b_j = 0

    for i in range(A_rows):
        row = A[i]
        for j in range(A_cols):
            elem = row[j]
            B[j][i] = elem

    print(B)
    return B


def test():
    B = [[1, 2], [5, 9]]
    r = B[1]
    r[0] = 124
    print(B[1])
    print(type(r))


# test()
if __name__ == '__main__':
    main([[1, 2, 3], [4, 5, 6]])
