# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q=deque([root])
        result=[]
        odd=True
        while q:
            count=0
            level_size=len(q)
            level=[]
            for _ in range(level_size):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not odd:  # Even levels are reversed
                level.reverse()   
            result.append(level)
            odd=not odd  # if even -> odd or if odd -> even level
        return result
        
