from typing import Optional, List

from utils.binary_tree_utils import BinaryTreeNode, build_binary_tree


# Time Complexity: O(n)
# Space Complexity: O(n)
def preorderTraversal(root: Optional[BinaryTreeNode]) -> List[int]:
    nodes_list = []

    def traverse(root):
        if not root:
            return

        nodes_list.append(root.val)
        traverse(root.left)
        traverse(root.right)

    traverse(root)

    return nodes_list


if __name__ == '__main__':
    arr = [1, None, 2, 3]
    root = build_binary_tree(arr)
    result = preorderTraversal(root)
    print(result)
