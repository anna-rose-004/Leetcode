class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result=[]
        if not root:
            return []
        def dfs(node,path,currentsum):
            if not node:
                return
            path.append(node.val)
            currentsum+=node.val
            if not node.left and not node.right and currentsum==targetSum: #if a leaf node and the sum matches
                result.append(list(path))
            
            dfs(node.left,path,currentsum)
            dfs(node.right,path,currentsum)
            path.pop()

        dfs(root,[],0)
        return result
        
        