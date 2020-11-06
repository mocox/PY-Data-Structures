class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack():
    def __init__(self):
        self.array = []
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):  # O(1)
        return self.array[self.length-1]

    def push(self, data):  # O(1)
        self.array.append(data)
        self.length += 1

    def pop(self):  # O(n)    :(
        self.array.pop()
        self.length -= 1


my_stack = Stack()

my_stack.push('1')
my_stack.push(2)
my_stack.push('3')
my_stack.pop()
print(my_stack)
