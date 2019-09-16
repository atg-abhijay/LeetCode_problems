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
        d = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [d[complement], i]

            d[num] = i


def main():
    print(Solution().twoSum([2, 7, 11, 15], 9))

if __name__ == '__main__':
    main()
