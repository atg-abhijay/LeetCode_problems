"""
URL of problem:
https://leetcode.com/problems/search-in-a-binary-search-tree/description/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if val == root.val:
            return root
        elif val > root.val:
            if root.right is not None:
                return self.searchBST(root.right, val)
            else:
                return None
        else:
            if root.left is not None:
                return self.searchBST(root.left, val)
            else:
                return None
