# This is a generic file for the trivial solution

from typing import Optional

from black import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    result = []

    def calculate_order(root, result, level) -> [List[int]]:
        if not root:
            return []

        if len(result) == level:
            result.append([])
        result[level].append(root.val)

        calculate_order(root.left, result, level + 1)
        calculate_order(root.right, result, level + 1)

        return result

    return calculate_order(root, result, 0)


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
