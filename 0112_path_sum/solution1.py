# Approach 1: Recursion
# The most intuitive way is to use a recursion here. One is going through the tree by considering at each step 
# the node itself and its children. 
# If node is not a leaf, one calls recursively hasPathSum method for its children with a sum decreased by the 
# current node value. If node is a leaf, one checks if the the current sum is zero, i.e if the initial sum was 
# discovered.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


obj = Solution()
root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
print(obj.hasPathSum(root, targetSum))


# Complexity Analysis:

# Time complexity : We visit each node exactly once, thus time complexity is O(N) where N is the number of nodes.
# Space complexity : In the worst case, the tree is completely unbalanced, e.g. each node has only one child node, 
# the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack 
# would be O(N). But in the best case (the tree is completely balanced), the height of the tree would be log(N). 
# Therefore, the space complexity in this case would be O(log(N)).