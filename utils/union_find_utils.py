class UnionFind:
    # Time Complexity: O(n) in the worst case, but nearly O(1) on average due to path compression.
    # Space Complexity: O(n) for the parent and size arrays.
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.size = [1] * size  # At the beginning - each set initially has one element

    # Finds the root of the set containing x with path compression.
    # This flattens the structure of the tree to speed up future queries.
    # Time Complexity: O(n) in the worst case, but Amortized O(1) in practice
    # Space Complexity: O(1)
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            # Path compression
            # Ensures that we flatten the structure of the tree whenever we find the root.
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Unites the sets containing x and y.
    # Returns True if the union was successful (i.e., x and y were in different sets).
    # Time Complexity: O(n) in the worst case, but Amortized O(1) in practice
    # Space Complexity: O(1)
    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            # Already in the same set
            return False

        # Union by size - attach the smaller tree under the larger tree
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

        return True

    # Checks if x and y are in the same set.
    # Time Complexity: O(n) in the worst case, but Amortized O(1) in practice
    # Space Complexity: O(1)
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    # Returns the size of the set containing x.

    # Time Complexity: O(n) in the worst case, but Amortized O(1) in practice
    # Space Complexity: O(1)
    def get_size(self, x):
        root_x = self.find(x)
        return self.size[root_x]


# Create a UnionFind instance with the specified size.
def create_union_find(size: int) -> UnionFind:
    return UnionFind(size)
