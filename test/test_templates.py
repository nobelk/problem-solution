from solution.node import Node

import sure

from solution.code_template import build_string
from solution.code_template import reverse_linked_list

def test_string_building():
    arr = ['s', 't', 'r', 'i', 'n', 'g']
    build_string(arr).should.equal('string')


def test_reverse_linked_list():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    reverse_linked_list(head).val.should.equal(10)