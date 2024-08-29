from collections import deque
from typing import Optional, List

from utils.binary_tree_utils import BinaryTreeNode, build_binary_tree


# Time Complexity: O(n)
# Space Complexity: O(n)
def averageOfLevels(root: Optional[BinaryTreeNode]) -> List[float]:
    average_levels = []
    queue = deque([root])

    while queue:
        queue_length = len(queue)
        level = []
        for _ in range(queue_length):
            node = queue.popleft()
            if node.val is not None:  # avoid adding None values to the level
                level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level:
            average_level = sum(level) / len(level)
            average_levels.append(average_level)

    return average_levels


if __name__ == '__main__':
    arr = [0, 5, 7, 8]
    root = build_binary_tree(arr)

    result = averageOfLevels(root)
    print(result)
