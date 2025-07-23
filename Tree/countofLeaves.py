def countLeaves(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1  # It's a leaf

    return countLeaves(root.left) + countLeaves(root.right)
