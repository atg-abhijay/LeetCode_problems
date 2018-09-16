"""
URL of problem:
https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
"""


def main(A):
    max_num = 0
    max_index = 0
    obj = enumerate(A)
    for index, num in obj:
        if num > max_num:
            max_num = num
            max_index = index

    print("Index with max value:", max_index)
    # return max_index


if __name__ == '__main__':
    main([0, 2, 1, 0])
