from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return

    print(root.val)  # preorder: Root, Left, Right
    traverse_tree(root.left)
    # print(root.val)  # inorder: Left, Root, Right
    traverse_tree(root.right)
    # print(root.val)  # postorder: Left, Right, Root
    return root


if __name__ == '__main__':
    # q_4 = TreeNode(15)
    # q_5 = TreeNode(7)
    q_2 = TreeNode(20)
    q_3 = TreeNode(9)
    q = TreeNode(3, q_2, q_3)
    result = traverse_tree(q)
