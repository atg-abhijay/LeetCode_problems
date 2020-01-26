"""
URL of problem:
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

from math import inf


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        root.depth = 1
        queue = [root]
        min_depth = inf

        while queue:
            node = queue.pop(0)
            has_children = False

            for child in [node.left, node.right]:
                if child:
                    has_children = True
                    child.depth = node.depth + 1
                    queue.append(child)

            if not has_children and min_depth > node.depth:
                min_depth = node.depth

        return min_depth
