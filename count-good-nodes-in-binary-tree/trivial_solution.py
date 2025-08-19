from utils.binary_tree_utils import BinaryTreeNode, build_binary_tree


# Time Complexity: O(n)
# Space Complexity: O(h)
def goodNodes(root: BinaryTreeNode) -> int:
    def dfs(node, max_value):
        if node is None:
            return 0

        count = 0

        # is a good node
        if node.val >= max_value:
            count = 1

        # Update max_value that the children should be greater or equal to
        new_max = max(max_value, node.val)

        # Recurse for left and right subtrees
        count += dfs(node.left, new_max)
        count += dfs(node.right, new_max)

        return count

    return dfs(root, root.val)


if __name__ == '__main__':
    arr = [3, 1, 4, 3, None, 1, 5]
    root = build_binary_tree(arr)
    result = goodNodes(root)
    print(result)
