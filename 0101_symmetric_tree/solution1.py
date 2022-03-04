# Approach 1: Recursive

# A tree is symmetric if the left subtree is a mirror reflection of the right subtree.

# Two trees are a mirror reflection of each other if:
# - Their two roots have the same value.
# - The right subtree of each tree is a mirror reflection of the left subtree of the other tree.
    

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            
            return t1.val == t2.val and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

        return isMirror(root, root)

# OR


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         return self.isMirror(root, root)
    
#     def isMirror(self, t1, t2):
#         if not t1 and not t2: return True
#         if not t1 or not t2: return False
#         return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)



root = [1,2,2,3,4,4,3]
obj = Solution()
print(obj.isSymmetric(root))


#  Complexity Analysis:

# Time complexity: O(n). Because we traverse the entire input tree once, the total run time is O(n), where n is 
# the total number of nodes in the tree.
# Space complexity : The number of recursive calls is bound by the height of the tree. In the worst case, the 
# tree is linear and the height is in O(n). Therefore, space complexity due to recursive calls on the stack is 
# O(n) in the worst case.