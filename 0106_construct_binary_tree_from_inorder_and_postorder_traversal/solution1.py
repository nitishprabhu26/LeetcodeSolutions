# Neetcode (similar to 105)

# For preorder traversal the first value is a root, then its left child, then its right child, etc. 
# For postorder traversal the last value is a root, then its right child, then its left child, etc.

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        # last element in postorder array is always going to be he root
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        print(mid)
        
        # 'mid' tells us how we are going to split right and left sides of the postorder and inorder array
        # we pass the new inorder and postorder sub arrays 
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1], )
        root.left = self.buildTree(inorder[:mid], postorder[:mid])

        return root


inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
obj = Solution()
print(obj.buildTree(inorder, postorder))


# Complexity Analysis:

# Time complexity : O(N) since each node is processed once.
# Space complexity : O(N), recursion stack
