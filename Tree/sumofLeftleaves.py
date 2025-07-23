from collections import deque
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        stack=deque([(root,False)])
        result=0
        while stack:
            node,isleft=stack.popleft()
            if not node.left and not node.right and isleft:
                result+=node.val
            if node.left:
                stack.append((node.left,True))
            if node.right:
                stack.append((node.right,False))
        return result
        