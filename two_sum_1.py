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
        for i, first_num in enumerate(nums[:-1]):
            j = i+1
            for second_num in nums[i+1:]:
                if first_num + second_num == target:
                    return [i, j]

                j += 1


def main():
    print(Solution().twoSum([2, 7, 11, 15], 9))

if __name__ == '__main__':
    main()
