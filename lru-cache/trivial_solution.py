from collections import OrderedDict


class LRUCache:
    # Space Complexity: O(n)
    def __init__(self, capacity: int):
        self.capacity = capacity
        # it's important in which order the data entered the cache
        self.cache = OrderedDict()  # orderedDict is implemented using Double Linked List and HashMap

    # Time Complexity: O(1)
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # Move the accessed key to the end to indicate it's most recently used
            self.cache.move_to_end(key)  # O(1)
            return self.cache[key]

    # Time Complexity: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # move it to the end
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the least recently used item
                self.cache.popitem(
                    last=False)  # O(1)
                # The last=False argument specifies that the first item (i.e., the oldest entry) should be removed.

        # Add the new item to the end (since we are using OrderedDict)
        # Update the value if the key already exists
        self.cache[key] = value


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # Output: 1
    cache.put(3, 3)  # evicts key 2
    print(cache.get(2))  # Output: -1 (not found)
    cache.put(4, 4)  # evicts key 1
    print(cache.get(1))  # Output: -1 (not found)
    print(cache.get(3))  # Output: 3
    print(cache.get(4))  # Output: 4
