# This is a generic file for the trivial solution
from typing import List

from utils.dag_utils import build_dag


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    paths = []

    def dfs(node, path):

        path.append(node)

        if node == len(graph) - 1:  # reached the target node
            paths.append(path.copy())
        else:
            for nb in graph[node]:
                dfs(nb, path)

        path.pop()

        return paths

    paths = dfs(0, [])

    return paths


if __name__ == '__main__':
    graph = [[1, 2], [3], [3], []]
    dag = build_dag(graph)
    result = allPathsSourceTarget(graph)
    print(result)
