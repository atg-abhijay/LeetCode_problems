"""
URL of problem:
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3419/
https://leetcode.com/problems/excel-sheet-column-number/
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet_dict = {}
        # integer for "A"
        num_value = 65
        for x in range(26):
            alphabet_dict[chr(num_value)] = num_value - 64
            num_value += 1

        col_number = 0
        rev_string = list(reversed(s))
        for idx, char in enumerate(rev_string):
            col_number += alphabet_dict[char] * pow(26, idx)

        return col_number


def main():
    print(Solution().titleToNumber("ZY"))


if __name__ == '__main__':
    main()
