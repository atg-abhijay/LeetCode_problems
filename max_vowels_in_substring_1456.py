"""
URL of problem:
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""


from re import findall


class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        num_vowels_substr = len(findall('[aeiou]', s[:k]))
        vowels = set('aeiou')
        leftmost_idx, max_vowels = 0, num_vowels_substr
        for char in s[k:]:
            leftmost_char = s[leftmost_idx]
            if leftmost_char in vowels:
                num_vowels_substr -= 1

            if char in vowels:
                num_vowels_substr += 1

            if num_vowels_substr > max_vowels:
                max_vowels = num_vowels_substr

            leftmost_idx += 1

        return max_vowels


def main():
    print(Solution().maxVowels("abciiidef", 3))


if __name__ == '__main__':
    main()
