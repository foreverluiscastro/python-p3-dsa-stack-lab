import ipdb

class Stack:

    def __init__(self, items = [], limit = 100):
        pass
        self.items = items[0:limit]
        self.limit = limit

    def isEmpty(self):
        pass
        return self.size() == 0

    def push(self, item):
        pass
        self.items.insert(0, item)

    def pop(self):
        pass
        return self.items.pop(0)

    def peek(self):
        pass
    
    def size(self):
        pass
        return len(self.items)

    def full(self):
        pass
        return self.size() >= self.limit

    def search(self, target):
        pass
        for idx, value in enumerate(self.items):
            if target == value:
                return idx
        
        return -1
