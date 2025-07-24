class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter=0
        def height(node):
            if not node:
                return 0
            left=height(node.left)
            right=height(node.right)
            self.max_diameter=max(self.max_diameter,left+right)
            return 1+max(left,right)
        height(root)
        return self.max_diameter
        