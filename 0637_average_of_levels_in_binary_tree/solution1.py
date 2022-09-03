# Approach #1 Using Depth First Search [Accepted]
# OR
# https://leetcode.com/problems/average-of-levels-in-binary-tree/discuss/105108/Python-Straightforward-with-Explanation


# Algorithm:
# One of the methods to solve the given problem is to make use of Depth First Search. In DFS, we try to exhaust 
# each branch of the given tree during the tree traversal before moving onto the next branch.
# To make use of DFS to solve the given problem, we make use of two lists count and res. 
# Here, count[i] refers to the total number of nodes found at the i^{th} level(counting from root at level 0) till 
# now, and res[i] refers to the sum of the nodes at the i^{th} level encountered till now during the Depth First 
# Search.
# We make use of a function average(t, i, res, count), which is used to fill the res and count array if we start 
# the DFS from the node t at the i^{th} level in the given tree. We start by making the function call 
# average(root, 0, res, count). After this, we do the following at every step:
# 1. Add the value of the current node to the res(or sum) at the index corresponding to the current level. 
#    Also, increment the count at the index corresponding to the current level.
# 2. Call the same function, average, with the left and the right child of the current node. Also, update the 
#    current level used in making the function call.
# 3. Repeat the above steps till all the nodes in the given tree have been considered once.
# 4. Populate the averages in the resultant array to be returned.


from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        count = []
        res = []
        
        def average(t, i, res, count):
            if not t:
                return
            
            if len(res) <= i:
                count.append(0)
                res.append(0)
                
            count[i] += 1
            res[i] += t.val
            average(t.left, i + 1, res, count)
            average(t.right, i + 1, res, count)
        
        average(root, 0, res, count)
        
        return [ res[i]/float(count[i]) for i in range(len(res))]


# OR
# using single array instead of 2 arrays for count and res


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        info = []
        def dfs(node, depth = 0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)

        return [s/float(c) for s, c in info]


# OR
# using dictionary to store instead of array
# https://youtu.be/MVxvNunB0d4


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        S = defaultdict(float)
        T = defaultdict(int)
        
        def dfs(node, h):
            if not node:
                return
                
            S[h] += node.val
            T[h] += 1
            
            dfs(node.left, h + 1)
            dfs(node.right, h + 1)
        
        dfs(root, 0)
        
        return [ S[i]/T[i] for i in range(len(S))]


root = [3,9,20,None,None,15,7]
obj = Solution()
print(obj.averageOfLevels(root))


# Complexity Analysis:
# Time complexity: O(n). The whole tree is traversed once only. Here, n refers to the total number of nodes in 
# the given binary tree.
# Space complexity : O(h). res and count array of size h are used. Here, h refers to the height(maximum number of 
# levels) of the given binary tree. Further, the depth of the recursive tree could go upto h only.