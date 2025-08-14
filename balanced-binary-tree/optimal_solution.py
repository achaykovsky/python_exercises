from typing import Optional

from utils.binary_tree_utils import BinaryTreeNode, print_tree_top_down


# Function to check if a binary tree is balanced.
# A binary tree is balanced if it is height-balanced,
# meaning the depth of the two subtrees of every node never differs by more than one.
# The height of a tree is equal to the depth of its deepest subtree, plus one for the root node:
# 1 + max(height of left subtree, height of right subtree)

# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the binary tree which is n in the worst case (skewed tree).
def get_height_imbalance(root: BinaryTreeNode) -> int:
    if not root:
        return 0

    # Check the height of the left and right subtrees
    left_height = get_height_imbalance(root.left)
    right_height = get_height_imbalance(root.right)
    # If either subtree is not balanced, return False
    if left_height == -1 or right_height == -1:
        return -1

    # The heights of the left and right subtrees differ by more than 1 -> whole tree is not balanced
    if abs(left_height - right_height) > 1:
        return -1

    # Return the height of the current node
    return max(left_height, right_height) + 1


def isBalanced(root: Optional[BinaryTreeNode]) -> bool:
    return get_height_imbalance(root) != -1


if __name__ == '__main__':
    q_4 = BinaryTreeNode(15)
    q_5 = BinaryTreeNode(7)
    q_2 = BinaryTreeNode(20, q_4, q_5)
    q_3 = BinaryTreeNode(9)
    q = BinaryTreeNode(3, q_2, q_3)
    print_tree_top_down(q)
    result = isBalanced(q)
    print(result)
