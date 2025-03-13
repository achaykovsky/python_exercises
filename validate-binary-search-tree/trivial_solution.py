from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def valid(node, left, right):
        if not node:
            return True

        current_value = node.val

        if not (left < current_value < right):
            return False

        return (valid(node.left, left, current_value) and
                valid(node.right, current_value, right))

    return valid(root, float('-inf'), float('inf'))  # initializing by -inf<x<inf


if __name__ == '__main__':
    # q_4 = BinaryTreeNode(3)
    # q_5 = BinaryTreeNode(5)
    q_2 = TreeNode(2)
    q_3 = TreeNode(2)
    q = TreeNode(2, q_2, right=q_3)
    result = isValidBST(q)
    print(result)
