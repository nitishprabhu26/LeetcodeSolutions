# Approach #2 (Iterative) [Accepted]
# Alternatively, we can solve the problem iteratively, in a manner similar to breadth-first search.
# Alhorithm:
# The idea is that we need to swap the left and right child of all nodes in the tree. So we create a queue 
# to store nodes whose left and right child have not been swapped yet. Initially, only the root is in the 
# queue. As long as the queue is not empty, remove the next node from the queue, swap its children, and add 
# the children to the queue. Null nodes are not added to the queue. Eventually, the queue will be empty and 
# all the children swapped, and we return the original root.

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque()
        queue.append(root)

        while queue:
            current = queue.popleft()
            
            # swap the children
            temp = current.left
            current.left = current.right
            current.right = temp
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root

        


root = [4,2,7,1,3,6,9]

obj = Solution()
print(obj.invertTree(root))


# Complexity Analysis:

# Time complexity: O(n). where n is the number of nodes in the tree.
# Since each node in the tree is visited / added to the queue only once.
# Space complexity: O(n), since in the worst case, the queue will contain all nodes in one level of the binary 
# tree. For a full binary tree, the leaf level has ceil[n/2] = O(n)leaves.
