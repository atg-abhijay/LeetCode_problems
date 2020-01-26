"""
URL of problem:
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        root.depth = 1
        queue = [root]
        max_depth = root.depth

        while queue:
            node = queue.pop(0)
            if max_depth < node.depth:
                max_depth = node.depth

            for child in node.children:
                child.depth = node.depth + 1
                queue.append(child)

        return max_depth
