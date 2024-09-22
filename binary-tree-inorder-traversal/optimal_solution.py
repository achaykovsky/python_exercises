from typing import Optional, List

from utils.binary_tree_utils import BinaryTreeNode, build_binary_tree


# Time Complexity: O(n)
# Space Complexity: O(h), which could be:
# O(logn) for a balanced tree or
# O(n) for a skewed tree.
def inorderTraversal(root: Optional[BinaryTreeNode]) -> List[int]:
    nodes_list = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        nodes_list.append(current.val)
        current = current.right

    return nodes_list


if __name__ == '__main__':
    arr = [1, None, 2, 3]
    root = build_binary_tree(arr)
    result = inorderTraversal(root)
    print(result)
