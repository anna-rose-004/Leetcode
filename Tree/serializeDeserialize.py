class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        result=[]
        q=[root]
        while q:
            node=q.pop(0)
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("null")
        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data :
            return None
        nodes=data.split(",")
        root=TreeNode(int(nodes[0]))
        q=[root]
        index=1

        while q:
            node=q.pop(0)
            if nodes[index]!="null":
                node.left=TreeNode(int(nodes[index]))
                q.append(node.left)
            index+=1

            if index<len(nodes) and nodes[index]!="null":
                node.right=TreeNode(int(nodes[index]))
                q.append(node.right)
            index+=1
        return root