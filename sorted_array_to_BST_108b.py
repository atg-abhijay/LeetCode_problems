"""
URL of problem:
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
"""
# ## ITERATIVE SOLUTION ## #
from math import floor, log2


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
        # ## ITERATIVE SOLUTION ## #
        # num_layers = floor(log2(len(nums)) + 1)
        # index = num_layers
        # count = 0
        # nodes = []
        # while num_layers > 0:
        #     node = TreeNode(nums[index])
        #     nodes.append(node)
        #     count += 1
        #     num_layers -= 1
        #     node.left = TreeNode(nums[index - num_layers])
        #     node.right = TreeNode(nums[index + num_layers])

        # pointer = int(floor(len(nums/2)))

        num_layers = floor(log2(len(nums)) + 1)
        indices_order = [0, num_layers]
        num_layers -= 1
        count, power, track = 1, 1, 0
        while num_layers > 0 and count < len(nums):
            left_child_index = indices_order[count] - num_layers
            if left_child_index < 0 or left_child_index >= len(nums):
                break
            else:
                indices_order.append(left_child_index)

            right_child_index = indices_order[count] + num_layers
            if right_child_index < 0 or right_child_index >= len(nums):
                break
            else:
                indices_order.append(right_child_index)

            count += 1
            track += 2
            if log2(track) == power:
                num_layers -= 1
                power += 1
                track = 1

        print(indices_order)

soln = Solution()
soln.sortedArrayToBST([7, 8, 9, 10, 11, 12])
