# Time Complexity: O(n) for put, get, and remove operations
# Space Complexity: O(n) to store the key-value pairs
class MyHashMap:
    def __init__(self):
        self.pairs = []  # pairs of (k,v)

    def put(self, key: int, value: int) -> None:
        for i, (k, v) in enumerate(self.pairs):
            if k == key:
                # update the value if key exists
                self.pairs[i] = (key, value)
                return
        # new pair
        self.pairs.append((key, value))

    def get(self, key: int) -> int:
        for k, v in self.pairs:
            if k == key:
                return v
        # pair doesn't exists
        return -1

    def remove(self, key: int) -> None:
        for i, (k, _) in enumerate(self.pairs):
            if k == key:
                self.pairs.pop(i)
                # remove the pair at index i
                return


if __name__ == '__main__':
    map = MyHashMap()
    map.put(1, 1)
    print(map.pairs)
    map.put(2, 2)
    print(map.pairs)
    map.get(1)
    map.get(3)
    map.put(2, 1)
    print(map.pairs)
    map.remove(2)
    print(map.pairs)
    map.get(2)
