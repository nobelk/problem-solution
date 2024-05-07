from collections import deque


def max_level_sum(root):
    max_level = 0
    level_count = 0
    max_sum = float('-inf')
    changed = False

    queue = deque()
    queue.append(root)

    while queue:
        node_count = len(queue)
        current_level_sum = 0
        level_count += 1
        changed = False
        for _ in range(node_count):
            node = queue.popleft()
            if node:
                changed = True
                current_level_sum += node.val
                queue.append(node.left)
                queue.append(node.right)
        if changed and current_level_sum > max_sum:
            max_sum = current_level_sum
            max_level = level_count
    return max_level
