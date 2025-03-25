from typing import List, Optional
from collections import deque

from utils.binary_tree_utils import BinaryTreeNode


# Time Complexity: O(n)
# Space Complexity: O(n)

# iterative approach
def sortedArrayToBST(arr: List[int]) -> Optional[BinaryTreeNode]:
    if not arr:
        return None

    mid = len(arr) // 2
    root = BinaryTreeNode(arr[mid])  # Create root
    queue = deque([(root, 0, len(arr) - 1)])  # Queue stores (node, left_idx, right_idx)

    while queue:  # O(n) space needed
        node, left, right = queue.popleft()  # Process current node

        mid = (left + right) // 2

        # Left child
        if left < mid:
            left_mid = (left + mid - 1) // 2
            node.left = BinaryTreeNode(arr[left_mid])
            queue.append((node.left, left, mid - 1))

        # Right child
        if mid < right:
            right_mid = (mid + 1 + right) // 2
            node.right = BinaryTreeNode(arr[right_mid])
            queue.append((node.right, mid + 1, right))

    return root


if __name__ == '__main__':
    arr = [-10, -3, 0, 5, 9]
    tree = sortedArrayToBST(arr)
