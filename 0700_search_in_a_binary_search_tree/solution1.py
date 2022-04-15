# Binary Search Tree:
# Binary Search Tree is a binary tree where the key in each node:
# - is greater than any key stored in the left sub-tree,
# - and less than any key stored in the right sub-tree.

# Approach 1: Recursion

# Algorithm:
# The recursion implementation is very straightforward:
# - If the tree is empty i.e. root == null or the value to find is here val == root.val, then return root.
# - If val < root.val - go to search into the left subtree searchBST(root.left, val).
# - If val > root.val - go to search into the right subtree searchBST(root.right, val).
# - Return root.


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or val == root.val:
            return root
        
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)

        
root = [4,2,7,1,3]
val = 2
obj = Solution()
print(obj.searchBST(root, val))


# Complexity Analysis:
# Time complexity : O(H), where H is a tree height. That results in O(logN) in the average case, and O(N) in the 
# worst case.
# Space complexity : O(H) to keep the recursion stack, i.e. O(logN) in the average case, and O(N) in the worst 
# case.
