class MyStack(object):

    def __init__(self):
        self.que1 = []
        self.que2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.que2.append(x)
        while self.que1:
            self.que2.append(self.que1.pop(0))
        self.que1, self.que2 = self.que2, self.que1

    def pop(self):
        """
        :rtype: int
        """
        return self.que1.pop(0)

    def top(self):
        """
        :rtype: int
        """
        if self.que1:
            return self.que1[0]
        else:
            return None

    def empty(self):
        """
        :rtype: bool
        """
        return not self.que1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()