def findClosestValueInBst(tree, target):
    return find_value_helper(tree, target, float('inf'))


def find_value_helper(tree, target, closest):
    if tree is None:
        print(f'Closest: {closest}')
        return closest
    if abs(target-tree.value) < abs(target-closest):
        closest = tree.value

    if target > tree.value:
        return find_value_helper(tree.right, target, closest)
    elif target < tree.value:
        return find_value_helper(tree.left, target, closest)
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
