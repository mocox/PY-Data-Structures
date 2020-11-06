class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):  # O(1)
        return self.top.data

    def push(self, data):  # O(1)
        newNode = Node(data)
        if self.bottom == None:
            self.bottom = newNode
            self.top = self.bottom
            self.length += 1
        else:
            self.top.next = newNode
            self.top = self.top.next
            self.length += 1

    def pop(self):  # O(n)    :(
        if self.bottom == None:
            print('ERROR: No elements in stack')
        else:
            i = 1
            current = self.bottom
            while i != self.length-1:
                current = current.next
                i += 1
            popped_value = current.next
            current.next = None
            self.top = current
            self.length -= 1
            return print('Popped value:', popped_value.data)

    def printSt(self):  # O(n)
        current = self.bottom
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print()


my_stack = Stack()

my_stack.push('1')
my_stack.push(2)
my_stack.push('3')
my_stack.pop()
my_stack.printSt()
