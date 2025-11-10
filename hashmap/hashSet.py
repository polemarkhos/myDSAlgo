class myHashSet:
    def __init__(self):
        self.buckets = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        bucket_index = key % 1000
        if key not in self.buckets[bucket_index]:
            self.buckets[bucket_index].append(key)

    def remove(self, key: int) -> None:
        bucket_index = key % 1000
        if key in self.buckets[bucket_index]:
            self.buckets[bucket_index].remove(key)

    def contains(self, key: int) -> bool:
        bucket_index = key % 1000
        return key in self.buckets[bucket_index]
