def invertBinaryTree(tree):
    if tree.left is None and tree.right is None:
        return
    tree.left, tree.right = tree.right, tree.left
    if tree.left is not None:
        invertBinaryTree(tree.left)
    if tree.right is not None:
        invertBinaryTree(tree.right)
