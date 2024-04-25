# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    result = []
    current_sum = 0
    if root is not None:
        branchSumsHelper(root, current_sum, result)
    return result


def branchSumsHelper(root, current_sum, result):
    if root is None:
        return
    current_sum += root.value
    if not root.left and not root.right:
        result.append(current_sum)
        return
    branchSumsHelper(root.left, current_sum, result)
    branchSumsHelper(root.right, current_sum, result)
