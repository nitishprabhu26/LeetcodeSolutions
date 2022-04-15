# Approach 2: Iteration

# Algorithm:
# To reduce the space complexity, one could convert recursive approach into the iterative one:
# While the tree is not empty root != null and the value to find is not here val != root.val:
# - If val < root.val - go to search into the left subtree root = root.left.
# - If val > root.val - go to search into the right subtree root = root.right.
# - Return root.


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root

        
# OR

# https://youtu.be/_E8JssPY1N4

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while curr != None:
            if curr.val == val: return curr
            if curr.val > val: curr = curr.left
            else: curr = curr.right
        return curr


root = [4,2,7,1,3]
val = 2
obj = Solution()
print(obj.searchBST(root, val))


# Complexity Analysis:
# Time complexity : O(H), where H is a tree height. That results in O(logN) in the average case, and O(N) in the 
# worst case.
# Space complexity : O(1) since it's a constant space solution.
