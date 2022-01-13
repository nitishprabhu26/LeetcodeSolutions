# Approach 2: Iteration
# The recursion above could be converted into the iteration

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            # insert into the right subtree
            if val > node.val:
                # insert right now
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            # insert into the left subtree
            else:
                # insert right now
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
        return TreeNode(val)


# OR - minor change in initial condition

# class Solution:
#     def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
#         if not root:
#             return TreeNode(val)
        
#         node = root
#         while node:
#             # insert into the right subtree
#             if val > node.val:
#                 # insert right now
#                 if not node.right:
#                     node.right = TreeNode(val)
#                     return root
#                 else:
#                     node = node.right
#             # insert into the left subtree
#             else:
#                 # insert right now
#                 if not node.left:
#                     node.left = TreeNode(val)
#                     return root
#                 else:
#                     node = node.left
#         return root


root = [4,2,7,1,3]
val = 5
obj = Solution()
print(obj.insertIntoBST(root, val))


# Complexity Analysis:

# Time complexity: O(H), where H is a tree height. That results in O(logN) in the average case, and O(N) in the 
# worst case.
# Space complexity : O(1) since it's a constant space solution.
