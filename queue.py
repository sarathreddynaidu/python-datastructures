from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def display(self):
        return self.buffer

pq = Queue()

pq.enqueue(139)
pq.enqueue(153)
pq.enqueue(181)

print(pq.display())

print(pq.dequeue())

print(pq.display())

print(pq.is_empty())

print(pq.size())

print(pq.dequeue())
print(pq.display())
print(pq.dequeue())
print(pq.display())

print(pq.is_empty())

print(pq.size())
