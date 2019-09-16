"""
URL of problem:
https://leetcode.com/problems/two-sum/
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in d and d[complement] != i:
                return [i, d[complement]]


def main():
    print(Solution().twoSum([2, 7, 11, 15], 9))

if __name__ == '__main__':
    main()
