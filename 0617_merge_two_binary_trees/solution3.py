# Approach #2 Iterative Method DFS [Accepted] using stack (modifying 1st tree without using extra tree)
# [we use our user defined stack inseatd of using recursion stack(run into stackoverflow)
# to get rid of stackoverflow issue: we go for iterative approach
# but here in case of a skewed tree we can get a out of memory issue (space complexiety : O(n) for a huge 
# input)]

# https://youtu.be/lw5swOzpFtE
# https://leetcode.com/problems/merge-two-binary-trees/discuss/173640/Python-Simple-Iterative-using-ListStack

# Algorithm:
# Here we traverse the two trees, but this time we make use of a stack to do so instead of making use of 
# recursion. Each entry in the stack stores data in the form [node_{tree1}, node_{tree2}]. Here, node_{tree1} 
# and node_{tree2} are the nodes of the first tree and the second tree respectively.
# We start off by pushing the root nodes of both the trees onto the stack. Then, at every step, we remove a 
# node pair from the top of the stack. For every node pair removed, we add the values corresponding to the two 
# nodes and update the value of the corresponding node in the first tree. Then, if the left child of the first 
# tree exists, we push the left child(pair) of both the trees onto the stack. 
# If the left child of the first tree doesn't exist, we append the left child(subtree) of the second tree to 
# the current node of the first tree. We do the same for the right child pair as well.
# If, at any step, both the current nodes are null, we continue with popping the next nodes from the stack.


from typing import Optional
import collections
# or
# from collections import Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        stack = collections.deque()
        stack.appendleft([root1, root2])
        while stack:
            curr = stack.popleft()
            
            if curr[1] is None:
                continue
                
            curr[0].val += curr[1].val
            
            if curr[0].left is None:
                curr[0].left = curr[1].left
            else:
                stack.appendleft([curr[0].left, curr[1].left])
                
            if curr[0].right is None:
                curr[0].right = curr[1].right
            else:
                stack.appendleft([curr[0].right, curr[1].right])
        
        return root1
        


root1 = [1, 3, 2, 5]
root2 = [2, 1, 3, None, 4, None, 7]
obj = Solution()
print(obj.mergeTrees(root1, root2))


# Complexity Analysis
# Time complexity : O(n). We traverse over a total of n nodes. Here, n refers to the smaller of the number of 
# nodes in the two trees.
# Space complexity : O(n). The depth of stack can grow upto n in case of a skewed tree.
