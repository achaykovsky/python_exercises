from typing import List, Optional

from utils.binary_tree_utils import BinaryTreeNode, print_inorder


# Time Complexity: O(n)
# Space Complexity: O(logn)
# The solution for sortedArrayToBST is a preorder DFS (Root -> Left -> Right)

# recursive approach
def sortedArrayToBST(nums: List[int]) -> Optional[BinaryTreeNode]:
    if not nums:
        return None

    def dfs(left: int, right: int) -> Optional[BinaryTreeNode]:
        if left > right:
            return None

        mid = (left + right) // 2
        root = BinaryTreeNode(nums[mid])

        # building the left subtree
        root.left = dfs(left, mid - 1)

        # building the right subtree
        root.right = dfs(mid + 1, right)

        return root

    return dfs(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    result = sortedArrayToBST(nums)
    print_inorder(result)
