"""
URL of problem:
https://leetcode.com/problems/sort-array-by-parity/description/
"""


def main(array):
    odd_nums = [x for x in array if x % 2 == 1]
    even_nums = [x for x in array if x % 2 == 0]

    # print(even_nums + odd_nums)
    return even_nums + odd_nums


if __name__ == '__main__':
    main([3, 1, 2, 4])
