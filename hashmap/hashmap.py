class myHashMap:
    def __init__(self):
        self.buckets = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        bucket_index = key % 1000
        if key in self.buckets[bucket_index]:
            self.buckets[bucket_index] = [key, value]
        elif key not in self.buckets[bucket_index]:
            self.buckets[bucket_index].extend([key, value])

    def get(self, key: int) -> int:
        bucket_index = key % 1000
        if key in self.buckets[bucket_index]:
            return self.buckets[bucket_index][1]
        else:
            return -1

    def remove(self, key: int) -> None:
        bucket_index = key % 1000
        if key in self.buckets[bucket_index]:
            self.buckets[bucket_index] = []
