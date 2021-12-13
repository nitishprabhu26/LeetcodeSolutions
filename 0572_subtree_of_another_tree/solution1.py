# Neetcode (Recursive DFS):
# https://youtu.be/E36O5SWp-LE

# Intuition:
# Check if, (strting from) each node in root tree matches with the subroot, if matches then subroot is a subtree 
# of root.
# we will have a helper function to check if 2 trees starting from the root provided are equal.

# Edge cases:
# if both trees are null: they are same
# if root is null and if subroot isnt null , then subroot is not a subtree of root
# But if root isnt null and if subroot is null , then subroot is a subtree of root, because one of the children 
# of leaf node of root is null

# Algorithm:
# Check if 2 trees are same, if yes return true. Else recursively call isSubtree on both of the child nodes

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    def sameTree(self, s, t):

        # both nodes are null, then they are still equal
        if not s and not t:
            return True

        # if one is null and the other isnt, they arent equal
        if not s or not t:
            return False

        # if value of both arent equal
        if s.val != t.val:
            return False

        # # can use this inplace of the above 2 if conditions, and the last return
        # if s and t and s.val == t.val:
        #     return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        # return False

        return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)

    
root = [3,4,5,1,2]
subRoot = [4,1,2]

obj = Solution()
print(obj.isSubtree(root, subRoot))


#  Complexity Analysis:
# Time complexity: O(s.t), s and t are size of both root and subroot tree.