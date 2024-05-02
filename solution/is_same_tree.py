# Definition for a binary tree node.
class TreeNode1(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    else:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
