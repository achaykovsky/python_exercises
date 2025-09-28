from typing import List


# DFS solution to check if a graph is bipartite.
# A bipartite graph can be colored using two colors such that no two adjacent nodes have the same color.


# Time Complexity: O(n * m) where n is the number of rows and m is the number of columns
# Space Complexity: O(n * m)
def isBipartite(graph: List[List[int]]) -> bool:
    colors = [0] * len(graph)

    for i in range(len(graph)):
        if colors[i] == 0:
            # Start DFS from the uncolored node (color 0)
            if not dfs(graph, colors, i, 1):

                return False
    return True


# Helper function to perform DFS and color the graph
# We have three options for coloring:

# The neighbor is the same color (1 or -1) -> False
# The neighbor has not been colored (0) -> Color it with the opposite color (-1 or 1)
# The neighbor can be colored with the opposite color (1 or -1) -> True
def dfs(graph: List[List[int]], colors: List[int], node: int, color: int) -> bool:
    colors[node] = color

    for neighbor in graph[node]:
        # the neighbor has the same color
        if colors[neighbor] == color:
            return False

        if colors[neighbor] == 0:
            # the neighbor has not been colored, color it with the opposite color
            if not dfs(graph, colors, neighbor, -color):
                return False

    return True


if __name__ == '__main__':
    # adjacency list representation of the graph
    graph = [[1, 4], [0, 2], [1], [4], [0, 3]]  # number of nodes = 5
    result = isBipartite(graph)
    print(result)
