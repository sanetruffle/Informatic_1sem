class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, index, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        for i in range(index - 1):
            current = current.next

        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def remove(self, index):
        current = self.head
        for i in range(index):
            current = current.next

        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

    def get(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def __len__(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

