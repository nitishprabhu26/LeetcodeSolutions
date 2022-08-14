# Neetcode:
# https://youtu.be/s6ATEkipzow
# OR
# Approach 1: Recursive Traversal with Valid Range
# https://leetcode.com/problems/validate-binary-search-tree/solution/

# (In actual - approach 1 of video solution on leetcode)

# Intuition
# On the first sight, the problem is trivial. Let's traverse the tree and check at each step if 
# node.right.val > node.val and node.left.val < node.val. 
# The problem is this approach will not work for all cases. Not only the right child should be larger than the 
# node but all the elements in the right subtree.
# One should keep both upper and lower limits for each node while traversing the tree, and compare the node 
# value not with children values but with these limits.

# Approach 1: Recursive Traversal with Valid Range
# The idea above could be implemented as a recursion. One compares the node value with its upper and lower 
# limits if they are available. Then one repeats the same step recursively for left and right subtrees.


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

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and
                   validate(node.left, low, node.val))
            # or
            # return (validate(node.left, low, node.val) and
            #        validate(node.right, node.val, high))

        return validate(root)


root = [5,1,4,None,None,3,6]
obj = Solution()
print(obj.isValidBST(root))


# Complexity Analysis:
# Time complexity : O(N) since we visit each node exactly once.
# Space complexity : O(N) since we keep up to the entire tree.(in case of a skewed tree)
