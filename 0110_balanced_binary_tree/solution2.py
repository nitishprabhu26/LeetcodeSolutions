# Approach 2: Bottom-up recursion
# https://leetcode.com/problems/balanced-binary-tree/solution/

# Intuition:
# In approach 1, we perform redundant calculations when computing height. In each call to height, we require that 
# the subtree's heights also be computed. Therefore, when working top down we will compute the height of a subtree 
# once for every parent. We can remove the redundancy by first recursing on the children of the current node and 
# then using their computed height to determine whether the current node is balanced.

# Algorithm:
# We will use the same height defined in the first approach. The bottom-up approach is a reverse of the logic of 
# the top-down approach since we first check if the child subtrees are balanced before comparing their heights. 
# The algorithm is as follows:
# Check if the child subtrees are balanced. If they are, use their heights to determine if the current subtree is 
# balanced as well as to calculate the current subtree's height.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # Return whether or not the tree at root is balanced while also returning the tree's height
    def isBalancedHelper(self, root: TreeNode):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1
        
        # Check subtrees to see if they are balanced. 
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0
        
        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
    
    
    def isBalanced(self, root: Optional[TreeNode]):
        return self.isBalancedHelper(root)[0]
        

root = [3,9,20,None,None,15,7]
obj = Solution()
print(obj.isBalanced(root))


# Complexity Analysis:

# Time complexity : O(n).
# For every subtree, we compute its height in constant time as well as compare the height of its children.
# Space complexity : O(n). The recursion stack may go up to O(n) if the tree is unbalanced.
