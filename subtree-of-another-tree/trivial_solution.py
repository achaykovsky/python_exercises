from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity: O(logn) + O(logm) where n,m are the sizes of the tree.
def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot:
        return True
    if not root:
        return False
    if sameTree(root, subRoot):
        return True

    return isSubtree(root.right, subRoot) or isSubtree(root.left, subRoot)


def sameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:  # both of the roots don't exist
        return True

    if not p or not q:  # one of the roots does not exist
        return False

    if p.val != q.val:  # values are different
        return False

    if p.val == q.val:  # the values are the same
        return sameTree(p.right, q.right) and sameTree(p.left, q.left)


if __name__ == '__main__':
    # Example 1
    # [4,1,2]
    p_2 = TreeNode(1)
    p_3 = TreeNode(2)
    p = TreeNode(4, p_2, p_3)

    # [3,4,5,1,2]
    q_4 = TreeNode(1)
    q_5 = TreeNode(2)
    q_2 = TreeNode(4, q_4, q_5)
    q_3 = TreeNode(5)
    q = TreeNode(3, q_2, q_3)
    result = isSubtree(q, p)
    print(result)
