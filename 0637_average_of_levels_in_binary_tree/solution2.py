# Approach #2 Breadth First Search [Accepted]
# https://www.geeksforgeeks.org/deque-in-python/ 
# (But actually, Left end is front, right is rear of the queue)(front and back doesnt matter)
# eg: appended all elements from left, (or even if it is right)
# deque([5, 4, 3, 2, 1, 0])
# queue[0] -> 5
# queue[-1] -> 0


# Algorithm:
# Another method to solve the given problem is to make use of a Breadth First Search. In BFS, we start by pushing 
# the root node into a queue. Then, we remove an element(node) from the front of the queue. For every node removed 
# from the queue, we add all its children to the back of the same queue. We keep on continuing this process till 
# the queue becomes empty. In this way, we can traverse the given tree on a level-by-level basis.
# But, in the current implementation, we need to do a slight modification, since we need to separate the nodes on 
# one level from that of the other.

# The steps to be performed are listed below:
# 1. Put the root node into the queue.
# 2. Initialize sum and count as 0 and temp as an empty queue.
# 3. Pop a node from the front of the queue. Add this node's value to the sum corresponding to the current level. 
#    Also, update the count corresponding to the current level.
# 4. Put the children nodes of the node last popped into the a temp queue(instead of queue).
# 5. Continue steps 3 and 4 till queue becomes empty. (An empty queue indicates that one level of the tree has 
#    been considered).
# 6. Reinitialize queue with its value as temp.
# 7. Populate the res array with the average corresponding to the current level.
# 8. Repeat steps 2 to 7 till the queue and temp become empty.
# At the end, resre is the required result.


import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            sum, count = 0, 0
            temp = collections.deque()
            
            while queue:
                n = queue.popleft()
                sum += n.val
                count += 1
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
                    
            queue = temp
            res.append(sum/count)
            
        return res

# OR

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            s = 0
            for i in range(size):
                node = queue.pop(0)
                s+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(s/size)
        return res


root = [3,9,20,None,None,15,7]
obj = Solution()
print(obj.averageOfLevels(root))


# Complexity Analysis:
# Time complexity: O(n). The whole tree is traversed atmost once. Here, n refers to the number of nodes in the 
# given binary tree.
# Space complexity : O(m). The size of queue or temp can grow upto atmost the maximum number of nodes at any 
# level in the given binary tree. Here, m refers to the maximum mumber of nodes at any level in the input tree.