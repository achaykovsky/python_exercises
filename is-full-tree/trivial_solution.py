from typing import Optional

from utils.binary_tree_utils import BinaryTreeNode, build_binary_tree


# Full Tree is a tree which has 0 or 2 children for each node (can't have one child)
def isFullTree(root: Optional[BinaryTreeNode]):
    if not root:
        return True

    if not root.left and not root.right:  # 0 children
        return True

    if root.left and root.right:  # 2 children
        return isFullTree(root.left) and isFullTree(root.right)
    return False


if __name__ == '__main__':
    arr = [1, 2, 3, None, 5]
    root = build_binary_tree(arr)
    result = isFullTree(root)
    print(result)
