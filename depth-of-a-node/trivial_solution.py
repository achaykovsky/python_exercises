# This is a generic file for the trivial solution
from black import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


NOT_FOUND = -1


def node_depth(root: Optional[TreeNode], x) -> int:
    depth = 0

    def calculate_depth(root: Optional[TreeNode], node_depth: int) -> int:
        if not root:
            return NOT_FOUND

        if root.val == x:
            return node_depth

        left_depth = calculate_depth(root.left, node_depth + 1)

        if left_depth != NOT_FOUND:
            return left_depth

        right_depth = calculate_depth(root.right, node_depth + 1)

        if right_depth != NOT_FOUND:
            return right_depth

        return NOT_FOUND

    return calculate_depth(root, depth)


if __name__ == '__main__':
    q_4 = TreeNode(6)
    q_5 = TreeNode(9)

    q_2 = TreeNode(2)

    q_3 = TreeNode(6, q_4, q_5)
    q = TreeNode(4, q_2, q_3)

    result = node_depth(q, x=4)
    print(result)
