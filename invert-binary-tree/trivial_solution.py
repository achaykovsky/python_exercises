from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return

    root.right, root.left = root.left, root.right

    invertTree(root.right)
    invertTree(root.left)

    return root


def traverse_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return

    traverse_tree(root.left)
    print(root.val)
    traverse_tree(root.right)

    return root


if __name__ == '__main__':
    q_4 = TreeNode(1)
    q_5 = TreeNode(3)

    q_6 = TreeNode(6)
    q_7 = TreeNode(9)

    q_2 = TreeNode(2, q_4, q_5)
    q_3 = TreeNode(7, q_6, q_7)
    q = TreeNode(4, q_2, q_3)
    print("Original Tree:")
    traverse_tree(q)

    result = invertTree(q)
    print("Inverted Tree:")
    traverse_tree(result)
