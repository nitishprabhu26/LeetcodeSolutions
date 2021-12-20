# Neetcode: Using Recursion - https://youtu.be/QHH6rIK3dDQ
# merging them in to a 'new' binary tree (as asked in the question)

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        root = TreeNode(v1+v2)

        root.left = self.mergeTrees(root1.left if root1 else None,
                                    root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None,
                                     root2.right if root2 else None)
        return root


# OR


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        t = TreeNode(root1.val+root2.val)
        t.left = self.mergeTrees(root1.left, root2.left)
        t.right = self.mergeTrees(root1.right, root2.right)
        return t


root1 = [1, 3, 2, 5]
root2 = [2, 1, 3, None, 4, None, 7]
obj = Solution()
print(obj.mergeTrees(root1, root2))


# Complexity Analysis:

# Time complexity: O(m+n) where m and n are the sizes of each of the input trees. actually O(n)
# Space complexity : O(n). extra tree created
