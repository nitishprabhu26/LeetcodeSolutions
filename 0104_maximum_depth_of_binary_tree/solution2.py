# Approach 1: Recursion -  implemented with the DFS strategy and recursion.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height)+1

# obj = Solution()
# print(obj.levelOrder(root))


# Complexity Analysis:

# Time complexity : we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes.
# Space complexity : in the worst case, the tree is completely unbalanced, e.g. each node has only left child node, 
# the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be 
# O(N). But in the best case (the tree is completely balanced), the height of the tree would be log(N). Therefore, 
# the space complexity in this case would be O(log(N)).
