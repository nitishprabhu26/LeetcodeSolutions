# Using Recursion
# The intuitive approach is to solve the problem by recursion. Here we demonstrate an example with the DFS (Depth First Search) strategy.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0 
        
        children = [root.left, root.right]
        # if we're at leaf node
        if not any(children):
            return 1
        
        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1 

# obj = Solution()
# root = [3,9,20,null,null,15,7]
# print(obj.levelOrder(root))


# Complexity Analysis:

# Time complexity : O(N) where N is the number of nodes.
# Space complexity : Space complexity : in the worst case, the tree is completely unbalanced, e.g. each node has only one child node, the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be O(N). But in the best case (the tree is completely balanced), the height of the tree would be log(N). Therefore, the space complexity in this case would be O(log(N)).

