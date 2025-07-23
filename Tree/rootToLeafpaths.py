class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result=[]
        def dfs(node,path):
            if not node:
                return
            path+=str(node.val)
            if not node.left and not node.right:  #if a leaf, add the value to the path
                result.append(path)
            else:
                path+="->" #adding arrow
                dfs(node.left,path)
                dfs(node.right,path)
        dfs(root,"")
        return result