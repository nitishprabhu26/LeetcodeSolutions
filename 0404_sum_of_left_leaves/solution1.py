# Approach 1: Iterative Tree Traversal (Pre-order)
# https://leetcode.com/problems/sum-of-left-leaves/solution/

# To get each left-leaf node's value, we need to "visit" each one. Note that because it is a sum we need, the order we visit the left-leaf 
# nodes in doesn't matter. As such, we can pick any algorithm that visits all nodes of the tree. The simplest such algorithm is an 
# iterative pre-order traversal

# When we visit each node, we'll need to know whether or not it is a left-leaf node: this is the main challenge in this problem. Remember 
# that once we're on a node, there is no link back up to its parent. This means that given a node, it is impossible to check whether or 
# not it is a left node unless we have an existing reference to its parent. There are a couple of strategies for handling this problem:
# 1. While we're at a node, we can check if its left-child is a leaf node (instead of trying to check if the node itself is a left child).
# 2. When we're ready to visit the children of a node, we can pass some extra information down telling the left child that it is a left 
#    child.
# The second strategy works well for the recursive implementation (Approach 2), but the first strategy is the best for the iterative, so 
# is what we'll go with here.

# Anyway, to do an iterative pre-order traversal, we start by putting the root onto a stack. Then, while the stack is non-empty, we take a 
# node off the top, check if the node's left child is a leaf node and then add that child's value to a total if it is. Finally, we put the 
# node's left child and right child onto the stack so that they can be visited too.

# Note that it doesn't matter whether we put the left or right child on the stack first. We just chose to put right and then left so that 
# left is the next off, thus matching the standard pre-order traversal code template.

# A pre-order traversal is a type of depth-first tree traversal. This is because it uses a stack to keep track of unvisited nodes. 
# Alternatively, we could have used a breadth-first tree traversal; using a queue to keep track of unvisited nodes instead of a stack. 
# This works because while the nodes are visited in a different order, this doesn't matter, as discussed above.



from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if root is None: 
            return 0

        def is_leaf(node):
            return node is not None and node.left is None and node.right is None

        stack = [root]
        total = 0
        while stack:
            sub_root = stack.pop()
            # Check if the left node is a leaf node.
            if is_leaf(sub_root.left):
                total += sub_root.left.val
            # If the right node exists, put it on the stack.
            if sub_root.right is not None:
                stack.append(sub_root.right)
            # If the left node exists, put it on the stack.
            if sub_root.left is not None:
                stack.append(sub_root.left)

        return total



root = [3,9,20,None,None,15,7]
obj = Solution()
print(obj.sumOfLeftLeaves(root))


# Complexity Analysis:
# Let N be the number of nodes in the tree.
# Time complexity : O(N).
# Each node is put onto the stack once, by its parent node. We know each node only has one parent because this is a tree. Therefore, each 
# node is only taken off, and processed, once. Processing a node is an O(1) operation. Therefore, we get a total time complexity of 
# N ⋅ O(1) = O(N).
# Space complexity : O(N) to keep the output structure which contains N node values.
# Remember that in complexity analysis, we're always looking at the worst case. The worst-case tree is one where we have a long "strand" 
# of left nodes, with each having a single right node.