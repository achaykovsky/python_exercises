from typing import Optional, List

from utils.binary_tree_utils import BinaryTreeNode, build_binary_tree


# Time Complexity: O(n)
# Space Complexity: O(n), and O(logn) if the tree is balanced

# left node->right node->current node
def postorderTraversal(root: Optional[BinaryTreeNode]) -> List[int]:
    nodes_list = []
    stack = [(root, False)]  # Store tuples of (node, visited)

    while stack:
        current, visited = stack.pop()
        if current:
            if visited:
                nodes_list.append(current.val)  # Node has been fully processed, add to result
            else:
                # Push nodes in reverse order for correct postorder processing
                stack.append((current, True))  # Push the current node (mark it as visited)
                stack.append((current.right, False))  # Push right child (not visited yet)
                stack.append((current.left, False))  # Push left child (not visited yet)

    return nodes_list


if __name__ == '__main__':
    arr = [1, None, 2, 3]
    root = build_binary_tree(arr)
    result = postorderTraversal(root)
    print(result)
