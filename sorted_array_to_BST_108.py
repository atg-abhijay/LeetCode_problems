"""
URL of problem:
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""
from math import floor


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])

        # start from the middle of the sorted
        # array. it will form the root of the BST.
        # call the method recursively on the left
        # and right halves of the leftover array
        # to construct the left and right subtrees.
        pointer = int(floor(len(nums)/2))
        node = TreeNode(nums[pointer])
        node.left = self.sortedArrayToBST(nums[0:pointer])
        if pointer != len(nums)-1:
            node.right = self.sortedArrayToBST(nums[pointer+1:])

        return node

soln = Solution()
soln.sortedArrayToBST([-10, -3, 0, 5, 9])
