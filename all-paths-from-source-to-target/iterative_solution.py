# This is a generic file for the trivial solution
from typing import List

from utils.dag_utils import build_dag


# Time Complexity: O(V+E*P) where P is the number of paths
# Space Complexity: O(P*V)
def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    paths = []

    stack = [(0, [0])]  # start point

    while stack:
        node, path = stack.pop()
        if node == len(graph) - 1:  # reached the target node
            paths.append(path)
        else:
            for nb in graph[node]:
                stack.append((nb, path + [nb]))
    return paths


if __name__ == '__main__':
    graph = [[1, 2], [3], [3], []]
    dag = build_dag(graph)
    result = allPathsSourceTarget(graph)
    print(result)
