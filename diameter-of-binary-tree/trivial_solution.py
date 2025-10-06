from typing import Optional

from utils.binary_tree_utils import BinaryTreeNode, build_binary_tree, print_tree_top_down


# Diameter of a binary tree is the length of the longest path between any two nodes in a tree
# The length of a path between two nodes is represented by the number of edges between them.

# Time Complexity: O(n)
# Space Complexity: O(h)

def diameterOfBinaryTree(root: Optional[BinaryTreeNode]) -> int:
    max_diameter = 0

    def height(node: Optional[BinaryTreeNode]) -> int:
        nonlocal max_diameter

        if not node:
            return 0

        left = height(node.left)
        right = height(node.right)

        # current diameter = left height + right height
        max_diameter = max(max_diameter, left + right)
        return 1 + max(left, right)

    height(root)
    return max_diameter


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    root = build_binary_tree(array)
    print("Original Tree:")
    print_tree_top_down(root)

    result = diameterOfBinaryTree(root)
    print("result", result)
