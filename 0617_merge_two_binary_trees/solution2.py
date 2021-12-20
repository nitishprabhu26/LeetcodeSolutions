# Approach #1 Using Recursion [Accepted]
# [without using a new tree, rather storing sum in the first tree itself]

# We can traverse both the given trees in a preorder fashion. At every step, we check if the current node 
# exists(isn't null) for both the trees. If so, we add the values in the current nodes of both the trees and 
# update the value in the current node of the first tree to reflect this sum obtained. At every step, we also 
# call the original function mergeTrees() with the left children and then with the right children of the 
# current nodes of the two trees. If at any step, one of these children happens to be null, we return the child 
# of the other tree(representing the corresponding child subtree) to be added as a child subtree to the calling 
# parent node in the first tree. At the end, the first tree will represent the required resultant merged binary 
# tree.

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1


root1 = [1, 3, 2, 5]
root2 = [2, 1, 3, None, 4, None, 7]
obj = Solution()
print(obj.mergeTrees(root1, root2))


# Complexity Analysis:
# Time complexity : O(m). A total of m nodes need to be traversed. m represents the minimum number of nodes 
# from the two given trees.
# Space complexity : O(m). The depth of the recursion tree can go upto m in the case of a skewed tree. In 
# average case, depth will be O(log m).
