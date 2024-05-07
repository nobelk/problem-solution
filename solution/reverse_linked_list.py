

def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev