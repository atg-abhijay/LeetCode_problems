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
        # ## ITERATIVE SOLUTION ## #
        post_order_trav = []
        if root:
            post_order_trav.append(root)
            index = 0
            while 1:
                node = post_order_trav[index]
                if node.children:
                    node.children.reverse()
                    post_order_trav = (post_order_trav[:index+1] +
                                       node.children +
                                       post_order_trav[index+1:])

                if index == len(post_order_trav)-1:
                    break

                index += 1

        post_order_vals = [node.val for node in reversed(post_order_trav)]
        return post_order_vals
