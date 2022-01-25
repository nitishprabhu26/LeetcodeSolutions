# Neetcode:
# https://youtu.be/0K0uCMYq5ng
# OR
# Approach 1: Preorder Traversal: Always Choose Left Middle Node as a Root
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/solution/

# Algorithm:
# Implement helper function helper(left, right), which constructs BST from nums elements between indexes 
# left and right:
# - If left > right, then there is no elements available for that subtree. Return None.
# - Pick left middle element: p = (left + right) // 2.
# - Initiate the root: root = TreeNode(nums[p]).
# - Compute recursively left and right subtrees: 
#   root.left = helper(left, p - 1), root.right = helper(p + 1, right).
# Return helper(0, len(nums) - 1).


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        
        return helper(0, len(nums) - 1)



nums = [-10,-3,0,5,9]
obj = Solution()
print(obj.sortedArrayToBST(nums))


# Complexity Analysis:

# Time complexity : O(N) since we visit each node exactly once.
# Space complexity : O(logN).
# The recursion stack requires O(logN) space because the tree is height-balanced. Note that the O(N) space 
# used to store the output does not count as auxiliary space, so it is not included in the space complexity.
