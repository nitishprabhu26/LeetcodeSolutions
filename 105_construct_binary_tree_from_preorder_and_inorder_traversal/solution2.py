# Approach 1: Recursion

# Algorithm:

# Build a hashmap to record the relation of value -> index for inorder, so that we can find the position of 
# root in constant time.
# Initialize an integer variable preorderIndex to keep track of the element that will be used to construct 
# the root.
# Implement the recursion function arrayToTree which takes a range of inorder and returns the constructed 
# binary tree:
# - if the range is empty, return null;
# - initialize the root with preorder[preorderIndex] and then increment preorderIndex;
# - recursively use the left and right portions of inorder to construct the left and right subtrees.
# Simply call the recursion function with the entire range of inorder.

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)


            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
obj = Solution()
print(obj.buildTree(preorder, inorder))


# Complexity Analysis:
# Let N be the length of the input arrays.

# Time complexity : O(N).
# Building the hashmap takes O(N) time, as there are N nodes to add, and adding items to a hashmap has a 
# cost of O(1), so we get O(N)⋅O(1)=O(N).
# Building the tree also takes O(N) time. The recursive helper method has a cost of O(1) for each call 
# (it has no loops), and it is called once for each of the N nodes, giving a total of O(N).
# Taking both into consideration, the time complexity is O(N).
# Space complexity : O(N).
# Building the hashmap and storing the entire tree each requires O(N) memory. The size of the implicit 
# system stack used by recursion calls depends on the height of the tree, which is O(N) in the worst case 
# and O(logN) on average. Taking both into consideration, the space complexity is O(N).