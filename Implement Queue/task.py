class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Trying to pop from an empty stack")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Trying to peek into an empty stack")
        return self.top.data

    def size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count

class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x):
        self.stack1.push(x)

    def pop(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()
