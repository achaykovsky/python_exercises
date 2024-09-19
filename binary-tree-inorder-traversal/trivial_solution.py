from typing import Optional, List

from utils.binary_tree_utils import BinaryTreeNode, build_binary_tree


# Time Complexity: O(n)
# Space Complexity: O(n)
def inorderTraversal(root: Optional[BinaryTreeNode]) -> List[int]:
    nodes_list = []

    def traverse(root):
        if not root:
            return

        traverse(root.left)
        nodes_list.append(root.val)
        traverse(root.right)

    traverse(root)

    return nodes_list


if __name__ == '__main__':
    arr = [1, None, 2, 3]
    root = build_binary_tree(arr)
    result = inorderTraversal(root)
    print(result)
