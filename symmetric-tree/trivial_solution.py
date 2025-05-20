from typing import Optional

from utils.tree_utils import build_tree, TreeNode

# Time Complexity: O(n)
# Space Complexity:O(h)
def isSymmetric(root: Optional[TreeNode]) -> bool:
    def is_mirror(root1: Optional[TreeNode], root2: Optional[TreeNode]):
        if not root1 and not root2:  # both roots are none -->trees are symmetric
            return True
        if not root1 or not root2:  # one root is none --> trees are not symmetric
            return False

        return root1.val == root2.val and is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)

    return is_mirror(root, root)


if __name__ == '__main__':
    arr = [1, 2, 2, 3, 4, 4, 7]
    root = build_tree(arr)
    result = isSymmetric(root)
    print(result)
