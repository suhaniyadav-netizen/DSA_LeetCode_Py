# Problem 100: Same Tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1: Store everything
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def rec(node, arr):
            if not node:
                arr.append("end")
                return None

            arr.append(node.val)
            rec(node.left, arr)     # Left Side of Tree
            rec(node.right, arr)    # Right side of Tree

        p_rec = []
        q_rec = []

        rec(p, p_rec)
        rec(q, q_rec)

        return p_rec == q_rec   # will be True when records are same ie p and q are same trees
    
# Time complexity: O(n)