# Approach 2: Iteration - Neetcode
# https://www.youtube.com/watch?v=6ZnyEApgFYg

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        levels = []
        if not root:
            return levels
        
        queue = deque()
        queue.append(root)
        
        while queue:
            queue_len=len(queue)
            level=[]
            
            for i in range(queue_len):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:        
                levels.append(level)
        
        return levels


# Complexity Analysis:

# Time complexity : O(N) since each node is processed exactly once.
# Space complexity : O(N) to keep the output structure which contains N node values.