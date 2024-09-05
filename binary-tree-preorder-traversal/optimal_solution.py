from typing import Optional, List

from utils.binary_tree_utils import BinaryTreeNode, build_binary_tree


# Time Complexity: O(n)
# Space Complexity: O(h)
def inorderTraversal(root: Optional[BinaryTreeNode]) -> List[int]:
    nodes_list = []
    current = root
    stack = []

    while current or stack:
        if current:
            nodes_list.append(current.val)
            stack.append(current.right)
            current = current.left
        else:
            current = stack.pop()

    return nodes_list


if __name__ == '__main__':
    arr = [1, None, 2, 3]
    root = build_binary_tree(arr)
    result = inorderTraversal(root)
    print(result)
