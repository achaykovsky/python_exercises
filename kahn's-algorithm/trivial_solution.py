from collections import deque, defaultdict
from typing import List


# Kahn's Algorithm for Topological Sorting
# Time Complexity: O(V+E) where V is the number of vertices and E is the number of edges
# Space Complexity: O(V+E) for storing the graph and in-degrees

def kahn_algorithm(n: int, edges: List[List[int]]) -> List[int]:
    in_degree = [0] * n
    graph = defaultdict(list)

    # Build the graph and calculate in-degrees
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    topological_order = []

    while queue:
        node = queue.popleft()
        topological_order.append(node)

        for neighbor in graph[node]:
            # Decrease in-degree of the neighbor
            in_degree[neighbor] -= 1

            # If in-degree becomes zero, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topological_order if len(topological_order) == n else []  # return empty list if there's a cycle


if __name__ == '__main__':
    n, edges = 6, [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    result = kahn_algorithm(n, edges)
    print(result)
