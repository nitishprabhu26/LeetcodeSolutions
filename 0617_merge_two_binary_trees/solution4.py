# Approach #2 Iterative Method BFS [Accepted] using stack (modifying 1st tree without using extra tree)
# will help in case of a skewed tree (helpful with reducing space complexity)
# https://youtu.be/lw5swOzpFtE


from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS solution
        if root1 is None:
            return root2
        queue = collections.deque()
        queue.appendleft([root1, root2])
        while queue:
            curr = queue.pop()
            
            if curr[1] is None:
                continue
                
            curr[0].val += curr[1].val
            
            if curr[0].left is None:
                curr[0].left = curr[1].left
            else:
                queue.appendleft([curr[0].left, curr[1].left])
                
            if curr[0].right is None:
                curr[0].right = curr[1].right
            else:
                queue.appendleft([curr[0].right, curr[1].right])
        
        return root1
        


root1 = [1, 3, 2, 5]
root2 = [2, 1, 3, None, 4, None, 7]
obj = Solution()
print(obj.mergeTrees(root1, root2))


# Complexity Analysis
# Time complexity : O(n). We traverse over a total of n nodes. Here, n refers to the smaller of the number of 
# nodes in the two trees.
# Space complexity : O(2^h). The max number of nodes that can be in any of the levels.
# performs better incomparision to DFS, in case of a skewed tree