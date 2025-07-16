from collections import deque
from typing import Optional, List

from utils.binary_tree_utils import BinaryTreeNode, build_binary_tree, print_tree_top_down


# Time Complexity: O(n)
# Space Complexity: O(n) for the queue used in level order traversal
def rightSideView(root: Optional[BinaryTreeNode]) -> List[int]:
    result = []
    if not root:
        return result

    queue = deque([root])

    while queue:
        # number of nodes at the current level
        level_length = len(queue)

        # Traverse all nodes at the current level
        for i in range(level_length):
            node = queue.popleft()

            # i is the index of the node in the current level
            # If it's the last node in the current level, add it to the result
            if i == level_length - 1:
                result.append(node.val)

            # Add left and right children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


if __name__ == '__main__':
    arr = [1, 2, 3, None, 5, None, 4]
    root = build_binary_tree(arr)
    print_tree_top_down(root)
    result = rightSideView(root)
    print(result)
