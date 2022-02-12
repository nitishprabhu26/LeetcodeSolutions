# Approach 2: Recursive Preorder Traversal.
# https://youtu.be/uB4R6zTLIaA (variable names changed as per solution found in leetcode discussion)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        def helper(node, num):
            if not node:
                return 0

            num = (num * 2) + node.val
            # num = (num << 1) | node.val
            
            if not node.left and not node.right:
                return num
            return helper(node.left, num) + helper(node.right, num)
        
        return helper(root, 0)


root = [1,0,1,0,1,0,1]
obj = Solution()
print(obj.sumRootToLeaf(root))

# Complexity Analysis:
# Time complexity: O(N), where N is a number of nodes, since one has to visit each node.
# Space complexity: up to O(H) to keep the recursion stack, where H is a tree height.