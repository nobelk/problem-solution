# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    return is_mirrored(tree.left, tree.right)

def is_mirrored(left, right):
    if left is not None and right is not None and left.value == right.value:
        return is_mirrored(left.left, right.right) and is_mirrored(left.right, right.left)
    return left == right