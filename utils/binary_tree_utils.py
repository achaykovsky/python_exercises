from collections import deque
from typing import Optional


# constructs a binary tree in a level-order fashion
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_binary_tree(arr):
    """
    Function to build a tree from a given array.
    arr: List of elements to insert in the tree.
    Returns the root of the constructed tree.
    """
    if not arr:
        return None

    root = BinaryTreeNode(arr[0])
    queue = deque([root])

    i = 1
    while queue and i < len(arr):
        current = queue.popleft()

        # Insert left child
        if i < len(arr) and arr[i] is not None:
            current.left = BinaryTreeNode(arr[i])
            queue.append(current.left)
        i += 1

        # Insert right child
        if i < len(arr) and arr[i] is not None:
            current.right = BinaryTreeNode(arr[i])
            queue.append(current.right)
        i += 1

    return root


def print_binary_tree_inorder(root):
    """
    Function to print the tree in inorder traversal.
    """
    if root is not None:
        print_binary_tree_inorder(root.left)
        print(root.val, end=' ')
        print_binary_tree_inorder(root.right)


def get_depth(root: Optional[BinaryTreeNode]) -> int:
    if not root:
        return 0
    q = deque([(root, 1)])
    max_depth = 0
    while q:
        node, depth = q.popleft()
        max_depth = max(max_depth, depth)
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))
    return max_depth


def print_tree_top_down(root: Optional[BinaryTreeNode]):
    if not root:
        print("[Empty Tree]")
        return

    depth = get_depth(root)
    max_width = 2 ** depth * 2

    q = deque([(root, 0, max_width // 2)])
    levels = [[] for _ in range(depth * 2 - 1)]

    while q:
        node, row, col = q.popleft()
        # Ensure row exists
        while len(levels[row]) < max_width:
            levels[row].append(" ")
        levels[row][col] = str(node.val)

        if node.left:
            if len(levels[row + 1]) < max_width:
                levels[row + 1] = [" "] * max_width
            levels[row + 1][col - 1] = "/"
            q.append((node.left, row + 2, col - 2))

        if node.right:
            if len(levels[row + 1]) < max_width:
                levels[row + 1] = [" "] * max_width
            levels[row + 1][col + 1] = "\\"
            q.append((node.right, row + 2, col + 2))

    for line in levels:
        print("".join(line).rstrip())
