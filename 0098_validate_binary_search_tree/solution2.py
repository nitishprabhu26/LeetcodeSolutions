# Approach 2: Iterative Traversal with Valid Range
# The above recursion could be converted into iteration, with the help of an explicit stack. DFS would be 
# better than BFS since it works faster here.
# (In actual - approach 1 of video solution on leetcode)


import math
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
            # or
            # stack.append((root.left, lower, val))
            # stack.append((root.right, val, upper))
        return True


root = [5,1,4,None,None,3,6]
obj = Solution()
print(obj.isValidBST(root))


# Complexity Analysis:
# Time complexity : O(N) since we visit each node exactly once.
# Space complexity : O(N) since we keep up to the entire tree.(in case of a skewed tree)

