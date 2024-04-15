from solution.tree_node import TreeNode


def dfs_recursive(root: TreeNode):
    if not root:
        return
    dfs_recursive(root.left)
    dfs_recursive(root.right)


def dfs(root: TreeNode):
    stack = [root]

    while stack:
        node = stack.pop()

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
