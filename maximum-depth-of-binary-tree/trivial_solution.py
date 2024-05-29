# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return max(maxDepth(root.right), maxDepth(root.left)) + 1


if __name__ == '__main__':
    # Example 1
    # [3,9,20,null,null,15,7]
    q_4 = TreeNode(15)
    q_5 = TreeNode(7)
    q_2 = TreeNode(20, q_4, q_5)
    q_3 = TreeNode(9)
    q = TreeNode(3, q_2, q_3)
    result = maxDepth(q)
    print(result)
