# BIG(O)
# Average Case                                           Worst Case
# Search  Insert  Delete  Insert/Remove from end/middle  Search  Insert  Delete  Insert/Remove from end/middle
# O(n)	  O(1)	  O(1)	  O(n)                           O(n)    O(1)	 O(1)    O(n)


# A single node of a double linked list
class Node():
    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList():
    # constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # add element to the end of the list
    def append(self, data):
        new_node = Node(data)
        new_node.prev = self.tail
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    # add element at the begining of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
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
        new_node.prev = leader
        follower.prev = new_node
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
    def printl(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
        print('Length = '+str(self.length))
