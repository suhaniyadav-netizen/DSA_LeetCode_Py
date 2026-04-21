# Problem 94. Binary Tree Inorder Traversal

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1: Recursion
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def explore(node):
            if node == None:
                return 
        
            explore(node.left)
            res.append(node.val)
            explore(node.right)

        explore(root)
        return res
    
# Time complexity: O(n)