class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            curr_node = self.root
            while True:
                if data > curr_node.data:
                    if curr_node.right == None:
                        curr_node.right = new_node
                        return
                    else:
                        curr_node = curr_node.right
                if data < curr_node.data:
                    if curr_node.left == None:
                        curr_node.left = new_node
                        return
                    else:
                        curr_node = curr_node.left

    def remove(self):
        pass

    def lookup(self, data):
        curr_node = self.root
        while True:
            if curr_node == None:
                return False
            elif curr_node.data == data:
                return True
            elif data > curr_node.data:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
# Inorder Traversal (We get sorted order of elements in tree)

    def printt(self, curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.data))
            self.printt(curr_node.right)

    def breadthFirstSearch(self):
        curr_node = self.root
        li = []
        queue = []
        queue.append(curr_node)
        while len(queue) > 0:
            curr_node = queue.pop(0)
            # print(curr_node.data)
            li.append(curr_node.data)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        return print(li)

    def breadthFirstSearchRecursive(self, queue, li):
        if len(queue) == 0:
            return print(li)
        curr_node = queue.pop(0)
        li.append(curr_node.data)
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)
        return self.breadthFirstSearchRecursive(queue, li)

    def DFSInorder(self):
        return traverseInOrder(self.root, [])

    def DFSPostorder(self):
        return traversePostOrder(self.root, [])

    def DFSPreorder(self):
        return traversePreOrder(self.root, [])


def traverseInOrder(node, li):
    if node.left:
        traverseInOrder(node.left, li)
    li.append(node.data)
    if node.right:
        traverseInOrder(node.right, li)
    return li


def traversePreOrder(node, li):
    li.append(node.data)
    if node.left:
        traverseInOrder(node.left, li)
    if node.right:
        traverseInOrder(node.right, li)
    return li


def traversePostOrder(node, li):
    if node.left:
        traverseInOrder(node.left, li)
    if node.right:
        traverseInOrder(node.right, li)
    li.append(node.data)
    return li


bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
bst.breadthFirstSearch()
bst.breadthFirstSearchRecursive([bst.root], [])
print(bst.DFSInorder())
print(bst.DFSPreorder())
print(bst.DFSPostorder())
x = bst.lookup(6)
print(x)
y = bst.lookup(99)
print(y)
bst.print_tree()
