class Solution(object):
    def countNodes(self, root):
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0
