# Approach 1: Depth-first Search [preferred]
# https://leetcode.com/problems/diameter-of-binary-tree/solution/
# https://www.w3schools.com/python/python_variables_global.asp


# Intuition:
# The key observation to make is: the longest path has to be between two leaf nodes.
# We know that the longest path in the tree would consist of a node, its longest left branch, and its longest 
# right branch. So, our algorithm to solve this problem will find the node where the sum of its longest left and 
# right branches is maximized. This would hint at us to apply Depth-first search (DFS) to count each node's branch 
# lengths, because it would allow us to dive deep into the leaves first, and then start counting the edges upwards. 

# To count the lengths of each node's left and right branches, we can implement a recursion function longestPath(), 
# which takes a TreeNode as input and returns the longest path from it to the leaf node. It will recursively visit 
# children nodes and retrieve the longest paths from them to the leaf first, and then add 1 to the longer one 
# before returning it as the longest path.

# In the midst of DFS, we also need to take the following two cases into account:
# 1. The current node's both left and right branches might be a part of the longest path;
# 2. One of the current node's left/right branches might be a part of the longest path.

# You will see we are going to address them by 
# 1) applying DFS to recursively find the longest branches starting with the node's left and right children; 
# 2) initializing a global variable 'diameter' to keep track of the longest path and updating it at each node with 
#    the sum of the node's left and right branches; 
# 3) returning the length of the longest branch between a node's left and right branches.

# Algorithm:
# - Initalize an integer variable diameter to keep track of the longest path we find from the DFS.
# - Implement a recursive function longestPath which takes a TreeNode as input. It should recursively explore the 
#   entire tree rooted at the given node. Once it's finished, it should return the longest path out of its left 
#   and right branches:
#   -   if node is None, we have reached the end of the tree, hence we should return 0;
#   -   we want to recursively explore node's children, so we call longestPath again with node's left and right 
#       children. In return, we get the longest path of its left and right children leftPath and rightPath;
#   -   if leftPath plus rightPath is longer than the current longest diameter found, then we need to update 
#       diameter;
#   -   finally, we return the longer one of leftPath and rightPath. Remember to add '1' as the edge connecting it 
#       with its parent.
# - Call longestPath with root.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path(node):
            if not node:
                return 0
            nonlocal diameter
            # recursively find the longest path in
            # both left child and right child
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            # update the diameter if left_path plus right_path is larger
            diameter = max(diameter, left_path + right_path)

            # return the longest one between left_path and right_path;
            # remember to add 1 for the path connecting the node and its parent
            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter


# or using global variable

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global diameter
        diameter = 0

        def longest_path(node):
            if not node:
                return 0
            global diameter
            # recursively find the longest path in
            # both left child and right child
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            # update the diameter if left_path plus right_path is larger
            diameter = max(diameter, left_path + right_path)

            # return the longest one between left_path and right_path;
            # remember to add 1 for the path connecting the node and its parent
            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter


# root = [1,2,3,4,5]
# obj = Solution()
# print(obj.diameterOfBinaryTree(root))


# Complexity Analysis:
# Let N be the number of nodes in the tree.
# Time complexity : O(N). This is because in our recursion function longestPath, we only enter and exit from each 
# node once. We know this because each node is entered from its parent, and in a tree, nodes only have one parent.
# Space complexity : O(N). The space complexity depends on the size of our implicit call stack during our DFS, 
# which relates to the height of the tree. In the worst case, the tree is skewed so the height of the tree is O(N). 
# If the tree is balanced, it'd be O(logN).
