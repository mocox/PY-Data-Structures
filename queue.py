class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.data

    def enqueue(self, data):
        newNode = Node(data)
        if self.first == None:
            self.first = newNode
            self.last = self.first
            self.length += 1
        else:
            self.last.next = newNode
            self.last = self.last.next
            self.length += 1

    def dequeue(self):
        if self.first == None:
            print('ERROR: No elements in queue')
        elif self.first.next == None:
            self.first = None
        else:
            self.first = self.first.next
            self.length -= 1

    def printQu(self):
        current = self.first
        while current is not None:
            print(current.data, end=' <- ')
            current = current.next
        print()


my_queue = Queue()

my_queue.enqueue('first')
my_queue.enqueue('second')
my_queue.enqueue('third')
my_queue.dequeue()
print(my_queue.peek())
my_queue.printQu()
