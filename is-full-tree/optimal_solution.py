from collections import deque
from typing import Optional

from utils.binary_tree_utils import BinaryTreeNode, build_binary_tree


# Full Tree is a tree which has 0 or 2 children for each node (can't have one child)
def isFullTree(root: Optional[BinaryTreeNode]) -> bool:
    if not root:
        return True

    queue = deque([root])

    while queue:
        node = queue.popleft()

        if (node.left and not node.right) or (not node.left and node.right):
            return False

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return True


if __name__ == '__main__':
    arr = [1, 2, 3, None, 5]
    root = build_binary_tree(arr)
    result = isFullTree(root)
    print(result)
