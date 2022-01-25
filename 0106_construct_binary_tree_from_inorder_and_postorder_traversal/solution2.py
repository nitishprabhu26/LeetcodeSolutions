# Approach 1: Recursion

# For preorder traversal the first value is a root, then its left child, then its right child, etc. 
# For postorder traversal the last value is a root, then its right child, then its left child, etc.

# Algorithm:
# Build hashmap value -> its index for inorder traversal.
# Return helper function which takes as the arguments the left and right boundaries for the current subtree 
# in the inorder traversal. These boundaries are used only to check if the subtree is empty or not. Here is 
# how it works helper(in_left = 0, in_right = n - 1):
# - If in_left > in_right, the subtree is empty, return None.
# - Pick the last element in postorder traversal as a root.
# - Root value has index in the inorder traversal, elements from in_left to index - 1 belong to the left 
#   subtree, and elements from index + 1 to in_right belong to the right subtree.
# - Following the postorder logic, proceed recursively first to construct the right subtree 
#   helper(index + 1, in_right) and then to construct the left subtree helper(in_left, index - 1).
# - Return root.

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(in_left, in_right):
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None
            
            # pick up the last element as a root
            val = postorder.pop()
            root = TreeNode(val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[val]
 
            # build right subtree
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)
            return root
        
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
obj = Solution()
print(obj.buildTree(inorder, postorder))


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