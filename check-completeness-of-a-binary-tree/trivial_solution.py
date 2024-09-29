from typing import Optional

from utils.binary_tree_utils import build_binary_tree, BinaryTreeNode


def find_levels(root, result, level):
    if not root:
        return

    if len(result) == level:  # result should be level + 1, so we add a new level if they are equal
        # example: for a binary tree with only the root, we have level 0
        result.append([])

    result[level].append(root.val)

    find_levels(root.left, result, level + 1)
    find_levels(root.right, result, level + 1)

    return result


def isCompleteTree(root: Optional[BinaryTreeNode]) -> bool:
    if not root:
        return True

    tree_levels = find_levels(root, [], 0)

    last_level = tree_levels[-1]

    for i in range(len(last_level)):
        if last_level[i] != last_level[i - 1] and last_level[i - 1] is None:
            return False

    return True


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, None, 7]
    root = build_binary_tree(arr)
    result = isCompleteTree(root)
    print(result)
