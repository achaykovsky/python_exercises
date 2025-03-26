from typing import List, Optional

from utils.binary_tree_utils import BinaryTreeNode, print_inorder


# Time Complexity: O(n)
# Space Complexity: O(logn)
# The solution for sortedArrayToBST is a preorder DFS (Root -> Left -> Right)

# recursive approach
def sortedArrayToBST(nums: List[int]) -> Optional[BinaryTreeNode]:
    if not nums:
        return None
    mid = len(nums) // 2
    root = BinaryTreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])  # Left half
    root.right = sortedArrayToBST(nums[mid + 1:])  # Right half
    return root


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    result = sortedArrayToBST(nums)
    print_inorder(result)
