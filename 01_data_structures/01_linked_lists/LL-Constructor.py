class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_linked_lsit = LinkedList(4)

print(my_linked_lsit.head.value)

"""
    def append(self, value):

    def prepend(self, value):

    def insert(self, index, value):
"""


