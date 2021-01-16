class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, value):
        h = 0
        for char in value:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
t["jan 1"] = 10
t["jan 5"] = 45
t["jan 11"] = 55
print(t.arr)
print(t["jan 5"])
del t["jan 11"]
print(t.arr)
print(t["jan 11"])
