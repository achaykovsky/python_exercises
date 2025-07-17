from typing import Optional, List

from utils.binary_tree_utils import BinaryTreeNode, build_binary_tree, print_tree_top_down


# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the binary tree, WC is O(n) for a skewed tree.

def leftSideView(root: Optional[BinaryTreeNode]) -> List[int]:
    result = []

    def dfs(node: Optional[BinaryTreeNode], level: int) -> None:
        if not node:
            return

        # If this is the first time we've reached this level, it's the leftmost node
        if level == len(result):
            result.append(node.val)

        dfs(node.left, level + 1)  # visit left first
        dfs(node.right, level + 1)  # then right

    dfs(root, 0)
    return result


if __name__ == '__main__':
    arr = [1, 2, 3, None, 5, None, 4]
    root = build_binary_tree(arr)
    print_tree_top_down(root)
    result = leftSideView(root)
    print(result)
