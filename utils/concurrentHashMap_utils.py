import threading


class ConcurrentHashMap:
    def __init__(self):
        self._lock = threading.Lock()
        self._map = {}

    def put(self, key, value):
        with self._lock:
            self._map[key] = value

    def get(self, key):
        with self._lock:
            return self._map.get(key, None)

    def remove(self, key):
        with self._lock:
            if key in self._map:
                del self._map[key]

    def contains_key(self, key):
        with self._lock:
            return key in self._map

    def size(self):
        with self._lock:
            return len(self._map)


if __name__ == '__main__':
    # Example usage
    concurrent_map = ConcurrentHashMap()
    concurrent_map.put("key1", "value1")
    print(concurrent_map.get("key1"))
    concurrent_map.remove("key1")
    print(concurrent_map.contains_key("key1"))
