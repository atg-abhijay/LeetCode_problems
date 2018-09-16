"""
URL of problem: https://leetcode.com/problems/flipping-an-image/description/
"""


def main():
    A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    B = []
    for row in A:
        r = reversed(row)
        p = []
        for num in r:
            # (1-num) gives us the
            # complement for 0s and 1s
            p.append(1-num)
        B.append(p)

    # print(B)
    return B

main()
