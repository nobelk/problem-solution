from typing import Optional
from tree_node import TreeNode


def is_leaf_similar_tree(root1: Optional[TreeNode], root2: Optional[TreeNode]):
    return list(all_leaves(root1)) == list(all_leaves(root2))


def all_leaves(root: TreeNode):
    if root:
        if not root.left and not root.right:
            yield root.val
        yield from all_leaves(root.left)
        yield from all_leaves(root.right)
