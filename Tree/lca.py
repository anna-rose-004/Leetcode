class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def lca(root,p,q):
            if not root or root==p or root==q:
                return root
            left=lca(root.left,p,q)
            right=lca(root.right,p,q)
            if left and right:
                return root
            return left or right
        return lca(root,p,q)