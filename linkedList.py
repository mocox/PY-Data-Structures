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

    # add element to the end of the list
    def append(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
        self.length += 1

    # add element at the begining of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    # add element at the given position of the list
    def insert(self, index, data):
        if index >= self.length:
            self.append(data)
        new_node = Node(data)
        leader = self.traverseToIndex(index-1)
        follower = leader.next
        leader.next = new_node
        new_node.next = follower
        self.length += 1

    # traverse to index
    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head
        while counter != index:
            currentNode = currentNode.next
            counter += 1
        return currentNode

    # remove element at the specified position
    def remove(self, index):
        if index >= self.length:
            print('Exception: Index Out Of Range!')
        leader = self.traverseToIndex(index-1)
        unwantedNode = leader.next
        leader.next = unwantedNode.next
        self.length -= 1

    # reverse the list
    def reverse(self):
        if not self.head.next:
            return self.head
        first = self.head
        self.tail = self.head
        second = first.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first

    # get length of the list
    def getLength(self):
        return self.length

    # get element at the given position
    def get(self, index):
        return self.traverseToIndex(index).data

    # set element at the given position
    def set(self, index, data):
        first = self.head
        counter = 0
        while counter != index:
            self.head = self.head.next
            counter += 1
        temp = self.head.data
        self.head.data = data
        self.head = first
        return temp

    # print list
    def printLL(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
