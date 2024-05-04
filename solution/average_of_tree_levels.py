from collections import deque

class TreeNodeL(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root):
    res = []

    queue = deque()
    queue.appendleft(root)

    while len(queue) > 0:
        level_count = len(queue)
        sum = 0.0
        count = 0
        while level_count > 0:
            node = queue.pop()
            sum += node.val
            count += 1
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
            level_count -= 1
        avg = sum / count
        res.append(avg)
    return res
