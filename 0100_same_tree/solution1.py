# Neetcode (Recursive DFS):
# https://youtu.be/vRbbcKXCxOw
# also,
# Approach 1: Recursion

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # both nodes are null, then they are still equal
        if not p and not q:
            return True
        
        # if one is null and the other isnt, they arent equal
        if not p or not q:
            return False
        
        # if value of both arent equal
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
    
p = [1,2,3] 
q = [1,2,3]

obj = Solution()
print(obj.isSameTree(p, q))


#  Complexity Analysis:

# Time complexity: O(p+q) i.e O(N). where p, q are size of both trees. Since we may need to iterate through 
# every single node in both the trees.
# Time complexity : O(N), where N is a number of nodes in the tree, since one visits each node exactly once.
# Space complexity : O(log(N)) in the best case of completely balanced tree and O(N) in the worst case of 
# completely unbalanced tree, to keep a recursion stack.