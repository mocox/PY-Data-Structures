# BIG(O)
# Average Case                                           Worst Case
# Search  Insert  Delete  Insert/Remove from end/middle  Search  Insert  Delete  Insert/Remove from end/middle
# O(n)	  O(1)	  O(1)	  O(n)                           O(n)    O(1)	 O(1)    O(n)


# A single node of a singly linked list
class Node():
    # constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# A Linked List class with single head node
class LinkedList():
    # constructor
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def append(self, data):
        newNode = Node(data)


# Creating a single node
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
