from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True  # this is the same tree
    if not p or not q:
        return False  # one of them is null so it's can't be the same tree
    if p.val != q.val:
        return False  # found different values

    if p.val == q.val:
        # validates the values on the left side and on the right side is equal
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == '__main__':
    # Example 1
    p_2 = TreeNode(2)
    p_3 = TreeNode(3)
    p = TreeNode(1, p_2, p_3)

    q_2 = TreeNode(2)
    q_3 = TreeNode(3)
    q = TreeNode(1, p_2, p_3)

    # Example 2
    # p_2 = TreeNode(2)
    # p = TreeNode(1, p_2)
    #
    # q_2 = TreeNode(2)
    # q = TreeNode(1, None, p_2)

    result = isSameTree(p, q)
    print(result)
