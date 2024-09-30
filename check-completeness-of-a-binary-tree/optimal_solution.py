from collections import deque
from typing import Optional

from utils.binary_tree_utils import build_binary_tree, BinaryTreeNode

# Time Complexity: O(n)
# Space Complexity: O(n)
def isCompleteTree(root: Optional[BinaryTreeNode]) -> bool:
    if not root:
        return True

    queue = deque([root])
    found_none = False
    while queue:
        node = queue.popleft()

        if not node:
            found_none = True
        else:
            if found_none:  # it means already encountered a none before
                return False
            queue.append(node.left)
            queue.append(node.right)

    return True


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, None, 7]
    root = build_binary_tree(arr)
    result = isCompleteTree(root)
    print(result)
