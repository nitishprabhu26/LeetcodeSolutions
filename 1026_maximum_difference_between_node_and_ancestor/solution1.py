# Approach #1: Recursion
# https://youtu.be/h5pZTLApTTo

# Intuition:
# Let's start from Brute Force.
# A typical Brute Force approach is to compare every node with its ancestors. In the worst case, we have to 
# compare every node-pair (when the tree is a single line).
# The time complexity would be O(N^2), given N is the number of nodes in the binary tree.

# Can we simplify it?
# Since the problem asks us the Maximum Difference, maybe we do not need to compare all ancestor for a given 
# node and we only need to compare the ancestors with Maximum value and Minimum value.
# Therefore, for a given node, we only need the maximum value and the minimum value from the root to this node.
# To achieve this, we can define a function helper to start recursion, which receives a node and two integers, 
# the maximum and minimum value of its ancestors, as input.
# In the function helper, we need to update the maximum difference, the current maximum value, and the current 
# minimum value.

# Algorithm:
# Step 1: Initialize a variable result to record the required maximum difference.
# Step 2: Define a function helper, which takes three arguments as input.
# The first argument is the current node, and the second and third arguments are the maximum and minimum 
# values along the root to the current node, respectively.
# In the function helper, update result and call helper on the left and right subtrees.
# Step 3: Run helper on the root. It will automatically do recursion on every node.
# Step 4: Finally, return result.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        # record the required maximum difference
        self.result = 0

        def helper(node, cur_max, cur_min):
            if not node:
                return
            # update `result`
            self.result = max(self.result, abs(cur_max-node.val),
                              abs(cur_min-node.val))
            # update the max and min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)

        helper(root, root.val, root.val)
        return self.result
        


root = [8,3,10,1,6,null,14,null,null,4,7,13]
obj = Solution()
print(obj.maxAncestorDiff(root))


# Complexity Analysis:
# Let N be the number of nodes in the binary tree.
# Time complexity: O(N) since we visit all nodes once.
# Space complexity: O(N) since we need stacks to do recursion, and the maximum depth of the recursion is the 
# height of the tree, which is O(N) in the worst case and O(log(N) in the best case.