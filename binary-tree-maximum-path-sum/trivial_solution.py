from typing import Optional

from utils.binary_tree_utils import BinaryTreeNode, build_binary_tree, print_binary_tree_inorder, print_tree_top_down


# Time Complexity: O(n)
# Space Complexity: O(h)
def maxPathSum(root: Optional[BinaryTreeNode]) -> int:
    max_sum = float('-inf')

    def calculate_max_sum(node: Optional[BinaryTreeNode]) -> int:
        nonlocal max_sum
        if not node:
            return 0

        # Recursively get the maximum sum from left and right subtrees
        left_subtree_sum = max(calculate_max_sum(node.left),
                               0)  # discard negative sums -> if the sum is negative, we'll sum it as 0
        right_subtree_sum = max(calculate_max_sum(node.right), 0)

        # Current path sum including the current node
        current_path_sum = node.val + left_subtree_sum + right_subtree_sum

        # Update the maximum path sum found until now
        max_sum = max(max_sum, current_path_sum)

        # Return the maximum sum from this node to its parent (either left or right)
        return node.val + max(left_subtree_sum, right_subtree_sum)

    calculate_max_sum(root)
    return max_sum


if __name__ == '__main__':
    arr = [-1, -2, -3]
    root = build_binary_tree(arr)
    print_tree_top_down(root)
    result = maxPathSum(root)
    print(result)
