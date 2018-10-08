"""
URL of problem:
https://leetcode.com/problems/leaf-similar-trees/description/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf_sequence1 = self.buildLeafSequence(root1)
        leaf_sequence2 = self.buildLeafSequence(root2)

        return leaf_sequence1 == leaf_sequence2

    def buildLeafSequence(self, root):
        # using a depth first approach
        # to locate the leaves
        leaf_sequence = []
        if root.left is None and root.right is None:
            leaf_sequence.append(root.val)
            return leaf_sequence
        else:
            if root.left is not None:
                leaf_sequence += self.buildLeafSequence(root.left)
            if root.right is not None:
                leaf_sequence += self.buildLeafSequence(root.right)

        return leaf_sequence
