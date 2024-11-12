# This is a generic file for the trivial solution

from typing import Optional

from black import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time Complexity: O(n)
# Space Complexity: O(n)

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    result = []

    def calculate_order(root: Optional[TreeNode], result: List[int], level: int) -> List[List[int]]:
        if not root:
            return []

        if len(result) == level:  # validates the result list already has a list allocated for the current level
            # result should be level + 1, so we add a new level if they are equal
            # example: for a binary tree with only the root, we have level 0
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
