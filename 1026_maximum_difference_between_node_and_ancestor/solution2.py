# Approach #2: Maximum Minus Minimum
# we just need to record the maximum and minimum values of all root-to-leaf paths and return the maximum 
# difference. To achieve this, we can record the maximum and minimum values during the recursion and return 
# the difference when encountering leaves.

# Algorithm:
# Step 1: Define a function helper, which takes three arguments as input and returns an integer.
# The first argument node is the current node, and the second argument cur_max and third argument cur_min are 
# the maximum and minimum values along the root to the current node, respectively.
# Function helper returns cur_max - cur_min when encountering leaves. Otherwise, it calls helper on the left 
# and right subtrees and returns their maximum.
# Step 2: Run helper on the root and return the result.


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

        def helper(node, cur_max, cur_min):
            # if encounter leaves, return the max-min along the path
            if not node:
                return cur_max - cur_min
            # else, update max and min
            # and return the max of left and right subtrees
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = helper(node.left, cur_max, cur_min)
            right = helper(node.right, cur_max, cur_min)
            return max(left, right)

        return helper(root, root.val, root.val)
        

root = [8,3,10,1,6,null,14,null,null,4,7,13]
obj = Solution()
print(obj.maxAncestorDiff(root))


# Complexity Analysis:
# Let N be the number of nodes in the binary tree.
# Time complexity: O(N) since we visit all nodes once.
# Space complexity: O(N) since we need stacks to do recursion, and the maximum depth of the recursion is the 
# height of the tree, which is O(N) in the worst case and O(log(N) in the best case.