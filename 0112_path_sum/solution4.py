# Approach : Neetcode
# https://youtu.be/LSKQyOz_P8I


from tkinter import N
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, curSum):
            if not node:
                return False

            curSum += node.val
            if not node.left and not node.right:  # if reach a leaf
                return curSum == targetSum
            
            return dfs(node.left, curSum) or dfs(node.right, curSum)
        
        return dfs(root, 0)


obj = Solution()
root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
print(obj.hasPathSum(root, targetSum))


# Complexity Analysis:

# Time complexity : We visit each node exactly once, thus time complexity is O(N) where N is the number of nodes.
# Space complexity : In the worst case, the tree is completely unbalanced, e.g. each node has only one child node, 
# the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack 
# would be O(N). But in the best case (the tree is completely balanced), the height of the tree would be log(N). 
# Therefore, the space complexity in this case would be O(log(N)).

# for an unbalanced tree, height of tree in O(N)
# and for a balanced tree, height of tree in O(log(N))