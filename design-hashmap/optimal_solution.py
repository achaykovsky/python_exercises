# Time Complexity: O(n/k) per operation on average, where n = number of keys, k = number of buckets
# Space Complexity: O(n) for storing key-value pairs


class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 10000
        self.buckets = [ListNode(-1, -1) for _ in range(self.size)]

    # Hash function to find the key
    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        # calculate the current placement inside the buckets
        current = self.buckets[self._hash(key)]
        while current.next:
            if current.next.key == key:
                # the key was found -> update to the new value
                current.next.val = value
                return
            current = current.next
        # it's a new key -> attach it to the end of the list
        current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        # calculate the current placement inside the buckets
        current = self.buckets[self._hash(key)]
        while current:
            if current.key == key:
                return current.val
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        # calculate the current placement inside the buckets
        current = self.buckets[self._hash(key)]
        while current and current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next


if __name__ == '__main__':
    map = MyHashMap()
    print(map.put(2, 2))
    print(map.get(2))
    print(map.put(1, 1))
    print(map.get(1))
    print(map.get(3))
    print(map.put(2, 1))
    print(map.get(2))
    print(map.remove(2))
    print(map.get(2))
