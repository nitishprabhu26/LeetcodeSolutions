# Approach #1 (Recursive) [Accepted]
# Algorithm:
# The inverse of an empty tree is the empty tree. The inverse of a tree with root r, and subtrees right and 
# left, is a tree with root r, whose right subtree is the inverse of left, and whose left subtree is the 
# inverse of right.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        root.left = right
        root.right = left

        return root
        

root = [4,2,7,1,3,6,9]

obj = Solution()
print(obj.invertTree(root))


# Complexity Analysis:

# Time complexity: O(n). where n is the number of nodes in the tree.
# Since each node in the tree is visited only once.
# Space complexity: Because of recursion,O(h) function calls will be placed on the stack in the worst case, 
# where h is the height of the tree. Because h∈O(n), the space complexity is O(n).

