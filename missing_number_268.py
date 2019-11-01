"""
URL of problem:
https://leetcode.com/problems/missing-number/
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_elements = len(nums) + 1
        nums_set = set(nums)
        for i in range(num_elements):
            if i not in nums_set:
                return i
