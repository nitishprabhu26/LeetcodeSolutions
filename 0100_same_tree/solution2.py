# Approach 2: Iteration

# Intuition:
# Start from the root and then at each iteration pop the current node out of the deque. Then do the same checks 
# as in the approach 1 :
# p and p are not None,
# p.val is equal to q.val,
# and if checks are OK, push the child nodes.

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q),])
        
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                    
        return True
        
    
p = [1,2,3] 
q = [1,2,3]

obj = Solution()
print(obj.isSameTree(p, q))


# Complexity Analysis:

# Time complexity : O(N) since each node is visited exactly once.
# Space complexity : O(log(N)) in the best case of completely balanced tree and O(N) in the worst case of 
# completely unbalanced tree, to keep a deque.