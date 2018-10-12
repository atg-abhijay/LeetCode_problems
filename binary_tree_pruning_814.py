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
        # evaluate the children of the root
        # recursively first. the children
        # may or may not get removed depending
        # on whether they have a subtree containing
        # 1. after that, evaluate the root itself.
        # if the root is 0 and has no children, then
        # it has to be set None. so, the tree gets
        # pruned after the evaluation of a node's children
        # and then the node itself.
        if root:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)

            if root.val == 0 and root.left is None and root.right is None:
                root = None

        return root
