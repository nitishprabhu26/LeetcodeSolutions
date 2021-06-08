# One liner
# https://www.geeksforgeeks.org/python-map-function/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return max(map(self.maxDepth, [root.left, root.right])) + 1 if root else 0

# obj = Solution()
# print(obj.levelOrder(root))