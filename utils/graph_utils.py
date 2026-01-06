# Utility functions for working with GraphNode objects


class GraphNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Function to print the graph starting from a given node

# This function performs a depth-first search (DFS) to print all nodes and their neighbors.

def print_graph(node: GraphNode) -> None:
    visited = set()

    def dfs(n: GraphNode) -> None:
        if n in visited:
            return
        visited.add(n)
        print(f"GraphNode {n.val} with neighbors: {[neighbor.val for neighbor in n.neighbors]}")
        for neighbor in n.neighbors:
            dfs(neighbor)

    dfs(node)
