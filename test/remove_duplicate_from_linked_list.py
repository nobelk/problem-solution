# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    prev = linkedList
    cur = linkedList.next
    while cur:
        if prev.value == cur.value:
            prev.next = cur.next
            cur = cur.next
        else:
            prev = cur
            cur = cur.next

    # Write your code here.
    return linkedList
