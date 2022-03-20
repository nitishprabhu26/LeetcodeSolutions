# Approach 1: Top-down recursion
# https://leetcode.com/problems/balanced-binary-tree/solution/

# Algorithm:
# First we define a function 'height' such that for any node p ∈ T,
# height(p) =   { -1                                            p is an empty subtree i.e. null
#               { 1 + max(height(p.left), height(p.right))      otherwise  

# Now that we have a method for determining the height of a tree, all that remains is to compare the height of 
# every node's children. A tree T rooted at r is balanced if and only if the height of its two children are within 
# 1 of each other and the subtrees at each child are also balanced. Therefore, we can compare the two child 
# subtrees' heights then recurse on each one.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # Compute the tree's height via recursion
    def height(self, root: TreeNode) -> int:
        # An empty tree has height -1
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # An empty tree satisfies the definition of a balanced tree
        if not root:
            return True
        
        # Check if subtrees have height within 1. If they do, check if the
        # subtrees are balanced
        return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        

root = [3,9,20,None,None,15,7]
obj = Solution()
print(obj.isBalanced(root))


# Complexity Analysis:

# Time complexity : O(n.logn).
# We go through every single node in the tree O(n), and for each node we run a recursive dfs to find height 
# of its subtree or to check if subtrees are balanced .i.e O(n^2)
# If our algorithm didn't have any early-stopping, we may end up having O(n^2) complexity if our tree is skewed 
# since height is bounded by O(n). However, it is important to note that we stop recursion as soon as the height 
# of a node's children are not within 1. In fact, in the skewed-tree case our algorithm is bounded by O(n), as 
# it only checks the height of the first two subtrees.
# Space complexity : O(n). The recursion stack may contain all nodes if the tree is skewed.
