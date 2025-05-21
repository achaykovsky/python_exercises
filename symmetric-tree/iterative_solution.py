from collections import deque
from typing import Optional

from utils.tree_utils import build_tree, TreeNode

# Time Complexity: O(n)
# Space Complexity:O(n)
def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    # Initialize a queue with the root node twice
    queue = deque([(root, root)])

    while queue:
        t1, t2 = queue.popleft()

        # Both nodes are None ---> continue to the next pair
        if not t1 and not t2:
            continue

        # One of the nodes is None ---> tree is not symmetric
        if not t1 or not t2:
            return False

        # The values of the nodes are different ---> tree is not symmetric
        if t1.val != t2.val:
            return False

        # Enqueue children in the mirror order
        queue.append((t1.left, t2.right))
        queue.append((t1.right, t2.left))

    # The loop was finished without finding any mismatches ---> the tree is symmetric
    return True


if __name__ == '__main__':
    arr = [1, 2, 2, 3, 4, 4, 3]
    root = build_tree(arr)
    result = isSymmetric(root)
    print(result)
