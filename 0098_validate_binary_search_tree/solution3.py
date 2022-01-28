# Approach 3: Recursive Inorder Traversal
# (In actual - approach 2 of video solution on leetcode)

# Left -> Node -> Right order of inorder traversal means for BST that each element should be smaller than the 
# next one.
# Hence the algorithm with O(N) time complexity and O(N) space complexity could be simple:
# - Compute inorder traversal list inorder.
# - Check if each element in inorder is smaller than the next one.

# Do we need to keep the whole inorder traversal list?
# Actually, no. The last added inorder element is enough to ensure at each step that the tree is BST (or not). 
# Hence one could merge both steps into one and reduce the used space.


import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)

root = [5,1,4,None,None,3,6]
obj = Solution()
print(obj.isValidBST(root))


# Complexity Analysis

# Time complexity : O(N) in the worst case when the tree is a BST or the "bad" element is a rightmost leaf.
# Space complexity : O(N) for the space on the run-time stack.(in case of a skewed tree)


