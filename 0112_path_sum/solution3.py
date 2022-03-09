# Approach : BFS + Queue

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        queue = [(root, targetSum - root.val)]
        
        while queue:
            # popping leftmost element
            curr, val = queue.pop(0)
            if not curr.left and not curr.right and val == 0:
                return True
            if curr.left:
                queue.append((curr.left, val-curr.left.val))
            if curr.right:
                queue.append((curr.right, val-curr.right.val))
        return False

# OR
# using deque

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        queue = deque([(root, targetSum - root.val),])
        
        while queue:
            # popping leftmost element
            curr, val = queue.popleft()
            if not curr.left and not curr.right and val == 0:
                return True
            if curr.left:
                queue.append((curr.left, val-curr.left.val))
            if curr.right:
                queue.append((curr.right, val-curr.right.val))
        return False



obj = Solution()
root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
print(obj.hasPathSum(root, targetSum))
