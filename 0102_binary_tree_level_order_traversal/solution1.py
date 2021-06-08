# Approach 1: Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels


# root = TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None},
#                         right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, 
#                                                 right: TreeNode{val: 7, left: None, right: None}}}


# obj = Solution()
# print(obj.levelOrder(root))


# Complexity Analysis:

# Time complexity : O(N) since each node is processed exactly once.
# Space complexity : O(N) to keep the output structure which contains N node values.
