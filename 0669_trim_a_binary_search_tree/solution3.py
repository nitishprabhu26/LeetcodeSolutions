# Approach : Neetcode: Recursion
# https://youtu.be/jwt5mTjEXGc


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        if not root:
            return None

        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # if root.val is included in the result
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

        
root = [1,0,2]
low = 1
high = 2
obj = Solution()
print(obj.trimBST(root, low, high))


# Complexity Analysis:
# Time complexity : O(N), where N is the total number of nodes in the given tree. We visit each node at most once.
# Space complexity : O(N). Even though we don't explicitly use any additional memory, the call stack of our 
# recursion could be as large as the number of nodes in the worst case.