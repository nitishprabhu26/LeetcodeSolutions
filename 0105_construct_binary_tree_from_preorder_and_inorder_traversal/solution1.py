# Neetcode:
# https://youtu.be/ihj4IQGZ2zc (explaination)

# The two key observations are: (same for solution2.py)
# 1. Preorder traversal follows Root -> Left -> Right, therefore, given the preorder array 'preorder', we 
# have easy access to the root which is preorder[0].
# 2. Inorder traversal follows Left -> Root -> Right, therefore if we know the position of Root, we can 
# recursively split the entire array into two subtrees.

# Now the idea should be clear enough. We will design a recursion function: it will set the first element of 
# preorder as the root, and then construct the entire tree. To find the left and right subtrees, it will look 
# for the root in inorder, so that everything on the left should be the left subtree, and everything on the 
# right should be the right subtree. Both subtrees can be constructed by making another recursion call.

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # when we are out of nodes to traverse
        if not preorder or not inorder:
            return None

        # first element in preorder array is always going to be he root
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # 'mid' tells us how we are going to split right and left sides of the preorder and inorder array
        # we pass the new inorder and preorder sub arrays 
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
obj = Solution()
print(obj.buildTree(preorder, inorder))


# Complexity Analysis:

# Time complexity : O(N) since each node is processed once.
# Space complexity : O(N), recursion stack
