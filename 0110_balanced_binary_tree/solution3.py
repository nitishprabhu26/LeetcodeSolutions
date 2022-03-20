# Approach : Neetcode
# https://youtu.be/QfJsau0ItOY

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            # empty tree case - its balanced and height 0
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            
            # balanced - check if tree is balanced from the root node(if left, right and also root is balanced)
            # both subtrees have to be balanced and also check if its balanced from the root node
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
        

root = [3,9,20,None,None,15,7]
obj = Solution()
print(obj.isBalanced(root))


# Complexity Analysis:
# Time complexity : O(n).
# Space complexity : O(n). The recursion stack may go up to O(n) if the tree is unbalanced.
