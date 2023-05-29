class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.limit = limit
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack is full. Cannot push item.")
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop item.")
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty")
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        for index, item in enumerate(self.items[::-1]):
            if item == target:
                return index
        return -1

    