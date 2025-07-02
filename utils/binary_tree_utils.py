from collections import deque
from typing import Optional


# constructs a binary tree in a level-order fashion
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_binary_tree(arr: [int]) -> Optional[BinaryTreeNode]:
    if not arr:
        return None

    nodes = [BinaryTreeNode(val) if val is not None else None for val in arr]
    for i in range(len(arr)):
        if nodes[i] is not None:
            left_i = 2 * i + 1
            right_i = 2 * i + 2
            if left_i < len(arr):
                nodes[i].left = nodes[left_i]
            if right_i < len(arr):
                nodes[i].right = nodes[right_i]
    return nodes[0]


def print_binary_tree_inorder(root: Optional[BinaryTreeNode]):
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
        while len(levels[row]) < max_width:
            levels[row].append(" ")
        levels[row][col] = str(node.val)

        # Calculate offset based on depth level
        level = row // 2
        gap = 2 ** (depth - level - 2)  # dynamic gap shrinking each level down

        if node.left:
            while len(levels[row + 1]) < max_width:
                levels[row + 1].append(" ")
            levels[row + 1][col - gap] = "/"
            q.append((node.left, row + 2, col - gap * 2))

        if node.right:
            while len(levels[row + 1]) < max_width:
                levels[row + 1].append(" ")
            levels[row + 1][col + gap] = "\\"
            q.append((node.right, row + 2, col + gap * 2))

    for line in levels:
        print("".join(line).rstrip())


def find_node(root: BinaryTreeNode, val: int) -> Optional[BinaryTreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)
