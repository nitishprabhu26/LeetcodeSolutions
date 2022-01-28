# Approach 4: Iterative Inorder Traversal
# Alternatively, we could implement the above algorithm iteratively.
# (In actual - approach 2 of video solution on leetcode)


import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True

root = [5,1,4,None,None,3,6]
obj = Solution()
print(obj.isValidBST(root))


# Complexity Analysis

# Time complexity : O(N) in the worst case when the tree is a BST or the "bad" element is a rightmost leaf.
# Space complexity : O(N) to keep stack.(in case of a skewed tree)
