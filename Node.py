class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def add_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def get_head(self):
        if self.head is None:
            return None
        return self.head.data

    def get_tail(self):
        if self.head is None:
            return None
        current = self.head
        while current.next is not None:
            current = current.next
        return current.data

    def exist(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    def remove(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
