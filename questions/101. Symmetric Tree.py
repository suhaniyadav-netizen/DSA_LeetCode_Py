class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        def rec_l(node,arr):
            if not node:
                arr.append("end")
                return None
            
            arr.append(node.val)
            rec_l(node.left, arr)     # Left Side of Tree
            rec_l(node.right, arr)    # Right side of Tree

        def rec_r(node,arr):
            if not node:
                arr.append("end")
                return None
            
            arr.append(node.val)
            rec_r(node.right, arr)     # Mirror approach of left node
            rec_r(node.left, arr)

        root_l = []
        root_r = []

        rec_l(root.left, root_l)
        rec_r(root.right, root_r)

        return root_l == root_r