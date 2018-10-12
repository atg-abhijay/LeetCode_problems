"""
URL of problem:
https://leetcode.com/problems/binary-tree-pruning/description/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)

            if root.val == 0 and root.left is None and root.right is None:
                root = None

        return root
