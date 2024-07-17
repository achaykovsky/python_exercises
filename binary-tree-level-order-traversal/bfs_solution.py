# This is a generic file for the trivial solution
from collections import deque
from typing import Optional

from black import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        queue_length = len(queue)
        level = []
        for _ in range(queue_length):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if level:
            result.append(level)

    return result


if __name__ == '__main__':
    q_4 = TreeNode(4)
    q_5 = TreeNode(5)
    q_6 = TreeNode(6)
    q_7 = TreeNode(5)

    q_3 = TreeNode(2, q_4, q_5)
    q_2 = TreeNode(3, q_6, q_7)

    q = TreeNode(1, q_2, q_3)

    result = levelOrder(q)
    print(result)
