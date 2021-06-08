# Approach 3: Iteration  -  with the help of the stack data structure.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        
        return depth

# obj = Solution()
# print(obj.levelOrder(root))


# Complexity Analysis:

# Time complexity :  O(N), where N is the number of nodes.
# Space complexity : in the worst case, the tree is completely unbalanced, e.g. each node has only left child node, 
# the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be 
# O(N). But in the best case (the tree is completely balanced), the height of the tree would be log(N). Therefore, 
# the space complexity in this case would be O(log(N)).
