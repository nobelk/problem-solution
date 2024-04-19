from typing import Optional
from solution.tree_node import TreeNode


def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    if root.val > val:
        return search_BST(root.left, val)
    else:
        search_BST(root.right, val)


def search_BST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    while root is not None and root.val != val:
        root = root.left if val < root.val else root.right
    return root
