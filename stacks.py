class StacksArray:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def pop(self):
        if self.isempty():
            print('Stack is empty')
            return
        return self.data.pop()

    def top(self):
        if self.isempty():
            print('Stack is empty')
            return
        return self.data[-1]


S = StacksArray()
S.push(1)
S.push(2)
S.push(3)
S.push(4)
print(S.data)
print(len(S))
S.pop()
S.pop()
S.pop()
print(S.isempty())
S.pop()
print(S.isempty())
print(S.data)
S.push(7)
S.push(9)
print(S.data)
print(S.top())