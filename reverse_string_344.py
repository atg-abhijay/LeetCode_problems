"""
URL of problem:
https://leetcode.com/problems/reverse-string/description/
"""


def main(string):
    """
    main method for running the program.
    Argument:
        string - any sort of string
    Prints:
        Reverse of given string
    """
    # convert the string to
    # a list, reverse the list
    # and combine it to get a
    # string once again.
    s_list = list(string)
    s_list.reverse()
    print(''.join(s_list))


if __name__ == '__main__':
    main(input("Input a string: "))
