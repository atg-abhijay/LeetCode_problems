"""
URL of problem: https://leetcode.com/problems/reverse-integer/description/
"""


def main(x):
    reversed_num = 0
    if x < 0:
        str_num = str(x)
        num_as_list = list(str_num)[1:]
        reverse_num_list = reversed(num_as_list)
        reversed_num = (-1) * int(''.join(reverse_num_list))
    else:
        str_num = str(x)
        num_as_list = list(str_num)
        reversed_num = int(''.join(reversed(num_as_list)))

    max_int = 2147483647
    if reversed_num < -1-max_int or reversed_num > max_int:
        print(0)
        # return 0
    else:
        print(reversed_num)
        # return reversed_num


if __name__ == '__main__':
    main(1534236469)
