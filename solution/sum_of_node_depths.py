

def sum_node_depths(root, depth=0):
    return depth if root is None else depth + sum_node_depths(root.left, depth+1) + sum_node_depths(root.right, depth+1)
