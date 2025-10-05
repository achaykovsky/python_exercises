from typing import List, Optional

from utils.binary_tree_utils import BinaryTreeNode, print_tree_top_down


# Time Complexity: O(n)
# Space Complexity: O(n)
def buildTree(preorder: List[int], inorder: List[int]) -> Optional[BinaryTreeNode]:
    # Map values to its index using inorder
    inorder_indices_map = {}
    for i, val in enumerate(inorder):
        inorder_indices_map[val] = i

    # Tracks the current index in the preorder list as we build the tree
    preorder_index = 0

    # build subtree from inorder[left:right+1]
    def build_subtree(left: int, right: int) -> Optional[BinaryTreeNode]:
        nonlocal preorder_index

        # no elements to construct the subtree
        if left > right:
            return None

        # Using preorder we are able to find the root node
        curr_val = preorder[preorder_index]
        preorder_index += 1

        # Find the index of this value in the inorder map
        inorder_index = inorder_indices_map[curr_val]

        # Create the root node
        current_node = BinaryTreeNode(curr_val)

        # Recursively build the left and right subtrees
        # Left subtree: elements before inorder_index
        current_node.left = build_subtree(left, inorder_index - 1)

        # Right subtree: elements after inorder_index
        current_node.right = build_subtree(inorder_index + 1, right)

        return current_node

    # Build the entire tree from the full inorder range
    return build_subtree(0, len(inorder) - 1)


if __name__ == '__main__':
    preorder = [5, 9, 2, 3, 4, 7]
    inorder = [2, 9, 5, 4, 3, 7]

    result = buildTree(preorder, inorder)
    print_tree_top_down(result)
    print(result)
