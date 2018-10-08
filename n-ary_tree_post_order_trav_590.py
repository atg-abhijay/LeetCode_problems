"""
URL of problem:
https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
"""


# Definition for a Node.
# class Node(object):
#     def __init__(self, val, children):
#         self.val = val
#         self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        post_order = []
        # checking if root is not null
        if root:
            if not root.children:
                post_order.append(root.val)
                return post_order

            # call postorder() on the
            # children of the root
            for child in root.children:
                post_order += self.postorder(child)

            # root gets appended
            # after its children
            post_order.append(root.val)

        return post_order
