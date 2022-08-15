# Approach #2 Using BFS and HashSet [Accepted]

# Algorithm:
# In this approach, the idea of using the set is the same as in the last approach. But, we can carry on the 
# traversal in a Breadth First Search manner, which is a very common traversal method used in Trees. The way BFS 
# is used can be summarized as given below. We start by putting the root node into a queue. We also maintain a set 
# similar to the last approach. 
# Then, at every step, we do as follows:
# 1. Remove an element, p, from the front of the queue.
# 2. Check if the element k-p already exists in the set. If so, return True.
# 3. Otherwise, add this element, p to the set. Further, add the right and the left child nodes of the current 
#    node to the back of the queue.
# 4. Continue steps 1. to 3. till the queue becomes empty.
# 5. Return false if the queue becomes empty.
# By following this process, we traverse the tree on a level by level basis.


import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hash_set = set()
        q = collections.deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            if node:
                if (k - node.val) in hash_set:
                    return True
                hash_set.add(node.val)
                q.append(node.right)
                q.append(node.left)
        
        return False


# OR
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/106067/C%2B%2BPython-Straight-Forward-Solution


class Solution:        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False


root = [5,3,6,2,4,None,7]
k = 9
obj = Solution()
print(obj.findTarget(root, k))


# Complexity Analysis:
# Time complexity : O(n). We need to traverse over the whole tree once in the worst case. Here, n refers to the 
# number of nodes in the given tree.
# Space complexity : O(n). The size of the set can grow atmost upto n.
