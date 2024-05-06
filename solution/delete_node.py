

class DeleteNodeSolution(object):
    def deleteNode(self, node):
        prev = None
        while node.next:
            node.val = node.next.val
            prev = node
            node = node.next
        prev.next = None