from solution.node import Node

# Efficient string building
def build_string(arr):
    result = []
    for c in arr:
        result.append(c)
    return "".join(result)


def reverse_linked_list(head: Node):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev