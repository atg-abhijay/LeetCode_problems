"""
URL of problem:
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
"""

from math import inf
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        lvl_sums = [-inf]
        max_sum, max_sum_lvl = lvl_sums[0], 0
        queue: List[TreeNode] = [root]
        root.lvl = 1
        while queue:
            node: TreeNode = queue.pop(0)
            if node.lvl == len(lvl_sums):
                lvl_sums.append(node.val)
                # At this stage, the sum for the previous level
                # is complete. Compare it with the current max
                # sum and check if the max sum needs to be updated.
                if lvl_sums[-2] > max_sum:
                    max_sum = lvl_sums[-2]
                    max_sum_lvl = len(lvl_sums) - 2
            else:
                lvl_sums[node.lvl] += node.val

            for child in [node.left, node.right]:
                if child:
                    child.lvl = node.lvl + 1
                    queue.append(child)

        return max_sum_lvl
