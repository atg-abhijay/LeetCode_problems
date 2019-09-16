"""
URL of problem:
https://leetcode.com/problems/contains-duplicate/
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        distinct_nums = set(nums)
        if len(nums) != len(distinct_nums):
            return True

        return False


def main():
    print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == '__main__':
    main()
