# Approach 1: Depth-first Search [not-preferred]
# Neetcode: https://youtu.be/bkxqA8Rfv04


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1
            
            # recursively find the longest path in
            # both left child and right child
            left = dfs(root.left)
            right = dfs(root.right)

            # update the diameter if left_path plus right_path is larger
            res[0] = max(res[0], 2 + left + right)

            # return the longest one between left_path and right_path;
            # remember to add 1 for the path connecting the node and its parent
            return max(left, right) + 1

        dfs(root)
        return res[0]


# root = [1,2,3,4,5]
# obj = Solution()
# print(obj.diameterOfBinaryTree(root))


# Complexity Analysis:
# Let N be the number of nodes in the tree.
# Time complexity : O(N). This is because in our recursion function dfs, we only enter and exit from each 
# node once. We know this because each node is entered from its parent, and in a tree, nodes only have one parent.
# Space complexity : O(N). The space complexity depends on the size of our implicit call stack during our DFS, 
# which relates to the height of the tree. In the worst case, the tree is skewed so the height of the tree is O(N). 
# If the tree is balanced, it'd be O(logN).
