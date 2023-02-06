class QueuesArray:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data) == 0

    def enqueue(self, e):
        self.data.append(e)

    def dequeue(self):
        if self.isempty():
            print('Queue is empty')
            return
        return self.data.pop(0)

    def first(self):
        if self.isempty():
            print('Queue is empty')
            return
        return self.data[0]


Q = QueuesArray()
Q.enqueue(2)
Q.enqueue(4)
Q.enqueue(6)
Q.enqueue(8)
print(Q.data)
print(len(Q))
Q.dequeue()
print(Q.data)
Q.dequeue()
Q.dequeue()
print(Q.data)
print(Q.isempty())
Q.enqueue(10)
print(Q.data)
print(Q.first())
