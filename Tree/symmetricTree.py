class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        def ismirror(left,right):
            if not left and not right:  # leaf node for both subtrees
                return True
            if not left or not right:  # one is a leaf node and other is not
                return False
            return (left.val == right.val and ismirror(left.right,right.left) 
            and ismirror(left.left,right.right))  # checking whether the values are same
        
        return ismirror(root.left,root.right)