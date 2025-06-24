# This module provides utility functions for working with directed acyclic graphs (DAGs).

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
def build_dag(graph):
    from collections import defaultdict
    dag = defaultdict(list)
    for node, edges in enumerate(graph):
        for edge in edges:
            dag[node].append(edge)
    return dag
