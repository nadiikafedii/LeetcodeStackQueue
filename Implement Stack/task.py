class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Trying to dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Trying to peek into an empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x):
        self.queue1.enqueue(x)

    def pop(self):
        if self.queue2.is_empty():
            while not self.queue1.is_empty():
                self.queue2.enqueue(self.queue1.dequeue())
        return self.queue2.dequeue()

    def top(self):
        if self.queue2.is_empty():
            while not self.queue1.is_empty():
                self.queue2.enqueue(self.queue1.dequeue())
        return self.queue2.peek()

    def empty(self):
        return self.queue1.is_empty() and self.queue2.is_empty()

obj = MyStack()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()