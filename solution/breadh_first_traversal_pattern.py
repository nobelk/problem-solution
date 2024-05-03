from collections import deque
from typing import List


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left, self.right = None, None
        self.next = None


def traverse(root: TreeNode) -> List[List[int]]:
    result = []
    if not root:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level)
    return result


def reverse_traverse(root: TreeNode) -> List[List[int]]:
    result = deque()
    if not root:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.appendleft(current_level)
    return list(result)


def zigzag_traverse(root: TreeNode) -> List[List[int]]:
    result = deque()
    if not root:
        return result
    queue = deque()
    queue.append(root)
    left_to_right = True
    while queue:
        level_size = len(queue)
        current_level = deque()
        for _ in range(level_size):
            current_node = queue.popleft()
            if left_to_right:
                current_level.append(current_node.value)
            else:
                current_level.appendleft(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(list(current_level))
        left_to_right = not left_to_right
    return list(result)


def level_average(root: TreeNode) -> List[List[int]]:
    result = []
    if not root:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = 0.0
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level += current_node.value
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level / level_size)
    return result


def min_tree_depth(root: TreeNode) -> int:
    if not root:
        return 0
    queue = deque()
    queue.append(root)
    min_depth = 0

    while queue:
        level_size = len(queue)
        min_depth += 1
        for _ in range(level_size):
            current_node = queue.popleft()
            if not current_node.left and not current_node.right:
                return min_depth
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)


def find_level_order_successor(root: TreeNode, needle: int) -> int:
    if not root:
        return -1

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.popleft()

            if current_node.value == needle:
                successor = queue.popleft()
                return successor.value

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

    return -1  # needle not found


def connect_next_level_order_siblings(root: TreeNode) -> None:
    if not root:
        return

    queue = deque()
    while queue:
        level_size = len(queue)
        previous_node = None
        for _ in range(level_size):
            current_node = queue.popleft()
            if previous_node:
                previous_node.next = current_node
            previous_node = current_node

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    return


def connect_all_level_order_siblings(root: TreeNode) -> None:
    if not root:
        return

    queue = deque()
    queue.append(root)
    previous_node = None

    while queue:
        current_node = queue.popleft()
        if previous_node:
            previous_node.next = current_node
        previous_node = current_node

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)
