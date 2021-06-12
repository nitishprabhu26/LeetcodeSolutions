#Approach 2: DFS Iteration
# We could also convert the above recursion into iteration, with the help of stack.
# The idea is to visit each leaf with the DFS strategy, while updating the minimum depth when we reach the leaf node.
# So we start from a stack which contains the root node and the corresponding depth which is 1. Then we proceed to the iterations: pop the current node out of the stack and push the child nodes. The minimum depth is updated at each leaf node.

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
        stack, min_depth = [(1, root),], float('inf')
        
        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((depth + 1, c))
        
        return min_depth  

# obj = Solution()
# root = [3,9,20,null,null,15,7]
# print(obj.levelOrder(root))


# Complexity Analysis:

# Time complexity : we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes.
# Space complexity : in the worst case we could keep up to the entire tree, that results in O(N) space complexity.
