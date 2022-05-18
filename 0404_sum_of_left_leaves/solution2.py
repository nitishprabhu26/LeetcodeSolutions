# Approach 2: Recursive Tree Traversal (Pre-order)
# https://leetcode.com/problems/sum-of-left-leaves/solution/

# Recall that recursive tree algorithms work by treating each node of the tree as the root of a subtree. The answer (i.e. the sum of left 
# leaf node values) is then found for each subtree by finding the answers for the left and right subtrees and combining (adding) them 
# together.

# The base case is that this subtree is a leaf node (i.e. the subtree only contains a single node; its root node). The value we return for 
# it depends on whether this subtree was to the left or the right of its parent. If it was to the left, we return its value. If it was to 
# the right, we return zero.

# The recursive case is that this subtree contains a left and/or right subtree (i.e. the subtree has more than just the root node in it). 
# We call the recursive function on the left and right subtrees, add their results together and return the added result.

# Like before though, we still have the problem of knowing whether or not the current subtree was to the left of its parent. With 
# recursion though, there is a far more elegant solution than before: we can simply have an additional boolean parameter on our recursive 
# function, specifying whether or not the subtree is a left one! Note that the top subtree is neither a left node, nor a right node, but 
# we pass in false for it, as the purpose of the parameter is to specify whether or not it is a left subtree.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        # An empty root is one of the test cases!
        if root is None:
            return 0

        def process_subtree(subtree, is_left):
            
            # Base case: This is a leaf node.
            if subtree.left is None and subtree.right is None:
                return subtree.val if is_left else 0
            
            # Recursive case: We need to add and return the results of the 
            # left and right subtrees.
            total = 0
            if subtree.left:
                total += process_subtree(subtree.left, True)
            if subtree.right:
                total += process_subtree(subtree.right, False)
            return total
        
        # Call the recursive function on the root node to start the process.
        # We need to be careful of the case that the root is empty.
        return process_subtree(root, False)



root = [3,9,20,None,None,15,7]
obj = Solution()
print(obj.sumOfLeftLeaves(root))


# We can simplify the code a bit by defining an additional base case: if the subtree is empty (null), then 0 should be returned. This 
# means we no longer need to do null-checks in three separate places. This is a pattern you will see a lot for recursive tree algorithms.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def process_subtree(subtree, is_left):
            
            # Base case: If this subtree is empty, return 0
            if subtree is None:
                return 0
            
            # Base case: This is a leaf node.
            if subtree.left is None and subtree.right is None:
                return subtree.val if is_left else 0
            
            # Recursive case: return result of adding the left and right subtrees.
            return process_subtree(subtree.left, True) + process_subtree(subtree.right, False)

        return process_subtree(root, False)


# Complexity Analysis:
# Let N be the number of nodes.
# Time complexity : O(N).
# The code within the recursive function is all O(1). The function is called exactly once for each of the N nodes. Therefore, the total 
# time complexity of the algorithm is O(N).
# Space complexity : O(N).
# In the worst case, the tree consists of nodes that form a single deep strand. In this case, the runtime-stack will have N calls to 
# processSubtree(...) on it at the same time, giving a worst-case space complexity of O(N).