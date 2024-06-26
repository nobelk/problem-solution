from collections import deque


# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            node = queue.popleft()
            array.append(node.name)
            for child in node.children:
                queue.append(child)

        return array
