"""
URL of problem:
https://leetcode.com/problems/reverse-string/description/
"""


def main(string):
    s_list = list(string)
    s_list.reverse()
    print(''.join(s_list))


if __name__ == '__main__':
    main(input("Input a string: "))
