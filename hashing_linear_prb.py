class Hash_Linear_Probe:
    def __init__(self):
        self.table_size = 10
        self.hashtable = [0] * self.table_size

    def hashcode(self, key):
        return key % self.table_size

    def Linear_probe(self, data):
        i = self.hashcode(data)
        j = 0
        while self.hashtable[(i+j) % self.table_size] != 0:
            j = j + 1
        return (i + j) % self.table_size

    def insert(self, data):
        i = self.hashcode(data)
        if self.hashtable[i] == 0:
            self.hashtable[i] = data
        else:
            i = self.Linear_probe(data)
            self.hashtable[i] = data

    def search(self, key):
        i = self.hashcode(key)
        j = 0
        while self.hashtable[(i+j) % self.table_size] != key:
            if self.hashtable[(i+j) % self.table_size] == 0:
                return False
            j = j + 1
        return True

    def display(self):
        print(self.hashtable)


H = Hash_Linear_Probe()
H.insert(24)
H.insert(28)
H.insert(54)
H.insert(62)
H.insert(84)
H.insert(96)
H.insert(18)
H.display()
print(H.search(34))
print(H.search(54))