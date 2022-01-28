# https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/
# Approach 1: Recursive Inorder Traversal
# To solve the problem, one could use the property of BST : inorder traversal of BST is an array sorted in 
# the ascending order.
# It's a very straightforward approach with O(N) time complexity. The idea is to build an inorder traversal 
# of BST which is an array sorted in the ascending order. Now the answer is the (k-1)th element of this array.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    
        return inorder(root)[k - 1]



root = [3,1,4,None,2]
k = 1
obj = Solution()
print(obj.kthSmallest(root, k))


# Complexity Analysis

# Time complexity : O(N) to build a traversal.
# Space complexity : O(N) to keep an inorder traversal.
