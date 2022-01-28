# Neetcode:
# https://youtu.be/5LUXSvjmGCw

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


root = [3, 1, 4, None, 2]
k = 1
obj = Solution()
print(obj.kthSmallest(root, k))


# Complexity Analysis

# Time complexity: O(H+k), where H is a tree height. This complexity is defined by the stack, which contains
# at least H+k elements, since before starting to pop out one has to go down to a leaf. This results in
# O(logN+k) for the balanced tree and O(N+k) for completely unbalanced tree with all the nodes in the left
# subtree.
# Space complexity: O(H) to keep the stack, where H is a tree height. That makes O(N) in the worst case of
# the skewed tree, and O(logN) in the average case of the balanced tree.
