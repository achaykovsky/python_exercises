from typing import Optional

from utils.graph_utils import GraphNode, print_graph


# Time Complexity: O(V + E) where V is the number of vertices (nodes) and E is the number of edges (connections)
# Space Complexity: O(V) for the cloned nodes mapping
def cloneGraph(node: Optional[GraphNode]) -> Optional[GraphNode]:
    if not node:
        return None

    # Create a mapping from original nodes to cloned nodes
    cloned_nodes = {}

    def dfs(node: GraphNode, cloned_nodes) -> GraphNode:
        if node in cloned_nodes:
            return cloned_nodes[node]

        # Create a new node for the cloned graph
        cloned_node = GraphNode(node.val)
        # Store the cloned node in the mapping
        cloned_nodes[node] = cloned_node

        # Recursively clone the neighbors
        for neighbor in node.neighbors:
            cloned_neighbor = dfs(neighbor, cloned_nodes)
            cloned_node.neighbors.append(cloned_neighbor)

        return cloned_node

    return dfs(node, cloned_nodes)


if __name__ == '__main__':
    node = GraphNode(1)
    node.neighbors = [GraphNode(2), GraphNode(3)]
    result = cloneGraph(node)
    print_graph(result)
