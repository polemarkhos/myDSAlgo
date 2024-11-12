class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        index = self.hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        index = self.hash(key)
        for i, pair in enumerate(self.buckets[index]):
            if pair[0] == key:
                self.buckets[index].pop(i)
