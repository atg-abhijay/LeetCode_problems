"""
URL of problem:
https://leetcode.com/problems/maximum-binary-tree/description/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return

        max_num = max(nums)
        max_idx = nums.index(max_num)

        root = TreeNode(max_num)

        left_nums = nums[:max_idx]
        right_nums = nums[max_idx+1:]

        root.left = self.constructMaximumBinaryTree(left_nums)
        root.right = self.constructMaximumBinaryTree(right_nums)

        return root

    def test():
        nums = [4, 5, 6]
        print(nums[3:])

    constructMaximumBinaryTree(self, [3,2,1,6,0,5])
