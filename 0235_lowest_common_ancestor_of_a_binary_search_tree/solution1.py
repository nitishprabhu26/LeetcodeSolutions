# Neetcode: (Iterative approach)
# https://youtu.be/gs2LMfuOR9k

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]
p = 2
q = 8
obj = Solution()
print(obj.lowestCommonAncestor(root, p, q))


# Complexity Analysis:

# Time Complexity: O(N), where N is the number of nodes in the BST. In the worst case we might be visiting
# all the nodes of the BST. (skewed tree) when all node only has one child and p,q are near the bottom.
# For a balanced BST, the time complexity may be O(log(n)) since we reduce the nodes to check by half after 
# each step.
# Space Complexity: O(1). 