# LRU Cache implementation using a doubly linked list and a hash map
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    # Space Complexity: O(n)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> ListNode
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # Time Complexity: O(1)
    def _remove_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Time Complexity: O(1)
    def _add_to_tail(self, node: Node):
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node

    # Time Complexity: O(1)
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove_node(node)  # we are using this node, so it should move to the MRU side of the Double LL
        self._add_to_tail(node)
        return node.value

    # Time Complexity: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove_node(self.cache[key])  # found a key that should be moved as the MRU node

        elif len(self.cache) >= self.capacity:
            lru_node = self.head.next  # exceeded the capacity, so the LRU node should be removed
            self._remove_node(lru_node)
            del self.cache[lru_node.key]

        new_node = Node(key, value)  # add the node to the MRU side (tail)
        self._add_to_tail(new_node)
        self.cache[key] = new_node


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
