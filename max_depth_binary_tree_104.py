"""
URL of problem:
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        root.depth = 1
        queue = [root]
        max_depth = root.depth

        while queue:
            node = queue.pop(0)
            if max_depth < node.depth:
                max_depth = node.depth

            for child in [node.left, node.right]:
                if child:
                    child.depth = node.depth + 1
                    queue.append(child)

        return max_depth
