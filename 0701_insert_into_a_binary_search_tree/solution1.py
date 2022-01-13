# Approach 1: Recursion

# The recursion implementation is very straightforward :
# If root is null - return TreeNode(val).
# If val > root.val - go to insert into the right subtree.
# If val < root.val - go to insert into the left subtree.
# Return root.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            # insert into the right subtree
            root.right = self.insertIntoBST(root.right, val)
        else:
            # insert into the left subtree
            root.left = self.insertIntoBST(root.left, val)
        return root


root = [4,2,7,1,3]
val = 5
obj = Solution()
print(obj.insertIntoBST(root, val))


# Complexity Analysis:

# Time complexity: O(H), where H is a tree height. That results in O(logN) in the average case, and O(N) in the 
# worst case.
# Space complexity : O(H) to keep the recursion stack, i.e. O(logN) in the average case, and O(N) in the worst 
# case.
