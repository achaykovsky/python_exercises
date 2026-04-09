from collections import defaultdict, deque
from typing import List


# Time Complexity: O(q * (V + E)) where q is the number of queries,
# V is the number of variables,
# and E is the number of equations
# Space Complexity: O(V + E)
def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    adj_list = defaultdict(list)  # adjacency list representation of the graph
    results = []

    for i, eq in enumerate(equations):
        a, b = eq  # unpack the equation
        adj_list[a].append([b, values[i]])  # direct edge
        adj_list[b].append([a, 1 / values[i]])  # reverse edge

    def bfs(src: str, target: str) -> float:
        if src not in adj_list or target not in adj_list:
            return -1  # if either node is not in the graph

        q, visited = deque(), set()
        q.append([src, 1])  # start with weight 1 at source since 1 is the multiplicative identity
        visited.add(src)

        while q:
            n, w = q.popleft()  # current node and the accumulated weight until node n
            if n == target:
                return w  # return the accumulated weight if target is reached
            for nb, weight in adj_list[n]:  # where nb is neighbor and weight is the edge weight
                if nb not in visited:
                    q.append([nb, w * weight])  # multiply weights along the path since it's a product of ratios
                    visited.add(nb)  # mark as visited
        return -1  # target not reachable from source

    for src, target in queries:
        # perform BFS for each query
        results.append(bfs(src, target))
    return results


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    result = calcEquation(equations, values, queries)
    print(result)
