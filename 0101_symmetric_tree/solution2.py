# Approach 2: Iterative

# Instead of recursion, we can also use iteration with the aid of a queue. Each two consecutive nodes in the queue 
# should be equal, and their subtrees a mirror of each other. Initially, the queue contains root and root. Then 
# the algorithm works similarly to BFS, with some key differences. Each time, two nodes are extracted and their 
# values compared. Then, the right and left children of the two nodes are inserted in the queue in opposite order. 
# The algorithm is done when either the queue is empty, or we detect that the tree is not symmetric (i.e. we pull 
# out two consecutive nodes from the queue that are unequal).
    

from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        q.append(root)
        
        while q:
            t1 = q.popleft()
            t2 = q.popleft()
            
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        
        return True


root = [1,2,2,3,4,4,3]
obj = Solution()
print(obj.isSymmetric(root))


#  Complexity Analysis:

# Time complexity: O(n). Because we traverse the entire input tree once, the total run time is O(n), where n is 
# the total number of nodes in the tree.
# Space complexity : There is additional space required for the search queue. In the worst case, we have to insert
# O(n) nodes in the queue. Therefore, space complexity is O(n).