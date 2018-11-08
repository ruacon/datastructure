class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def print(self):
        print(self.items)

class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def deque(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def print(self):
        print(self.items)

class Dequeue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def print_Dequeue(self):
        print(self.items)

# Stack object.
# s = Stack()
# print(s.isEmply())
# s.push(4)
# s.push('dog')
# s.push(True)
# print(s.pop())
# print(s.pop())
# print(s.size())

# Queue object
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# q.enqueue(6)
# q.enqueue(7)
# print(q.size())
# q.deque()
# q.deque()
# print(q.size())

# Dequeue object.
# d = Dequeue()
# d.addFront(1)
# d.addFront(2)
# d.addFront(3)
# d.print_Dequeue()
# d.addRear(3)
# d.addRear(4)
# d.addRear(5)
# d.print_Dequeue()
# d.removeFront()
# d.print_Dequeue()
# d.removeRear()
# d.print_Dequeue()


