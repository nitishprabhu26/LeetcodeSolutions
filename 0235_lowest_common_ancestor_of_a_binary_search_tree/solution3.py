# Approach 2: Iterative Approach

# Algorithm
# The steps taken are also similar to approach 1. The only difference is instead of recursively calling the 
# function, we traverse down the tree iteratively. This is possible without using a stack or recursion since 
# we don't need to backtrace to find the LCA node. In essence of it the problem is iterative, it just wants 
# us to find the split point. The point from where p and q won't be part of the same subtree or when one is 
# the parent of the other.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:

            # Value of current node or parent node.
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:    
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node


root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]
p = 2
q = 8
obj = Solution()
print(obj.lowestCommonAncestor(root, p, q))


# Complexity Analysis:

# Time Complexity: O(N), where N is the number of nodes in the BST. In the worst case we might be visiting
# all the nodes of the BST. (skewed tree) when all node only has one child and p,q are near the bottom.
# For a balanced BST, the time complexity may be O(log(n)) since we reduce the nodes to check by half after 
# each step.
# Space Complexity: O(1). 
