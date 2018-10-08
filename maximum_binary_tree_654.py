"""
URL of problem:
https://leetcode.com/problems/maximum-binary-tree/description/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


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

        # calling the method on the 2 lists
        # to construct the left and right
        # subtrees. the values returned form
        # the children of the root node.
        root.left = self.constructMaximumBinaryTree(left_nums)
        root.right = self.constructMaximumBinaryTree(right_nums)

        return root
