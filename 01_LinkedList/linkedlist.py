class Node:
    """
    Node of a singly linked list.
    Each node contains a value and a reference to the next node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Singly linked list implementation with full feature support.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def append(self, value):
        """Add a node to the end of the list. O(1)"""
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1

    def prepend(self, value):
        """Add a node to the beginning of the list. O(1)"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self._length == 0:
            self.tail = new_node
        self._length += 1

    def insert(self, index, value):
        """Insert a node at a specific index. O(n)"""
        if index < 0 or index > self._length:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.prepend(value)
            return
        if index == self._length:
            self.append(value)
            return

        new_node = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self._length += 1

    def delete(self, index):
        """Delete a node at a specific index. O(n)"""
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            if self._length == 1:
                self.tail = None
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            target = current.next
            current.next = target.next
            if index == self._length - 1:
                self.tail = current
        self._length -= 1

    def pop(self):
        """Remove and return the last element. O(n)"""
        if self._length == 0:
            raise IndexError("Pop from empty list")
        if self._length == 1:
            value = self.head.value
            self.head = self.tail = None
            self._length = 0
            return value
        current = self.head
        while current.next != self.tail:
            current = current.next
        value = self.tail.value
        current.next = None
        self.tail = current
        self._length -= 1
        return value

    def remove(self, value):
        """Remove first occurrence of value. O(n)"""
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                    if self._length == 1:
                        self.tail = None
                else:
                    previous.next = current.next
                    if current == self.tail:
                        self.tail = previous
                self._length -= 1
                return True
            previous = current
            current = current.next
        return False

    def find(self, value):
        """Return the index of the first occurrence of value. O(n)"""
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def get(self, index):
        """Get the value at a specific index. O(n)"""
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def set(self, index, value):
        """Set the value at a specific index. O(n)"""
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def reverse(self):
        """Reverse the linked list in-place. O(n)"""
        previous = None
        current = self.head
        self.tail = current
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        self.head = previous

    def print_list(self):
        """Print the current values in the list."""
        current = self.head
        if not current:
            print("Linked List is empty.")
            return
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values) + " -> None")

    def __len__(self):
        return self._length

    def __iter__(self):
        """Enable iteration over the list."""
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        """Return a string representation of the list."""
        return " -> ".join(str(v) for v in self) + " -> None"


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()       # 1 -> 2 -> 3 -> None

ll.set(1, 42)
ll.print_list()       # 1 -> 42 -> 3 -> None
