# Using Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, node, level):
        if level > self.max_depth:
            self.max_depth = level

        if node.left:
            self.helper(node.left, level+1)
        if node.right:
            self.helper(node.right, level+1)

    def maxDepth(self, root: TreeNode) -> int:
        self.max_depth = 0

        if not root:
            return self.max_depth

        self.helper(root, 0)
        return self.max_depth+1

# obj = Solution()
# print(obj.levelOrder(root))


# Complexity Analysis:

# Time complexity : O(N) since each node is processed exactly once.
# Space complexity : O(1)
