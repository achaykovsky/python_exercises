# This is a generic file for the trivial solution
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    result = []
    queue = deque([root])
    level = 0

    while queue:
        queue_length = len(queue)
        level_nodes = []
        for _ in range(queue_length):
            node = queue.popleft()

            # processing the node
            level_nodes.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # changing the order of the nodes in an non-even level
        if level % 2 == 1:
            level_nodes.reverse()

        result.append(level_nodes)
        level += 1

    return result


if __name__ == '__main__':
    q_4 = TreeNode(4)
    q_5 = TreeNode(5)
    q_6 = TreeNode(6)
    q_7 = TreeNode(5)

    q_3 = TreeNode(2, q_4, q_5)
    q_2 = TreeNode(3, q_6, q_7)

    q = TreeNode(1, q_2, q_3)

    result = zigzagLevelOrder(q)
    print(result)
