"""
URL of problem:
https://leetcode.com/problems/verifying-an-alien-dictionary/
"""


from itertools import tee


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        value, order_dict = 0, {}
        for letter in order:
            order_dict[letter] = value
            value += 1

        first_itr, second_itr = tee(words)
        next(second_itr)
        for first_word, second_word in zip(first_itr, second_itr):
            equal_so_far = True
            for f_char, s_char in zip(first_word, second_word):
                if order_dict[f_char] < order_dict[s_char]:
                    equal_so_far = False
                    break
                elif order_dict[f_char] > order_dict[s_char]:
                    return False

            if equal_so_far and len(first_word) > len(second_word):
                return False

        return True


def main():
    print(Solution().isAlienSorted(
          ["app", "apps", "app"], "abcdefghijklmnopqrstuvwxyz"))


if __name__ == '__main__':
    main()
