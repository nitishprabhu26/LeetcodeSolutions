# Approach #3 Using BST [Accepted]

# Algorithm:
# In this approach, we make use of the fact that the given tree is a Binary Search Tree. Now, we know that the 
# inorder traversal of a BST gives the nodes in ascending order. Thus, we do the inorder traversal of the given 
# tree and put the results in a list which contains the nodes sorted in ascending order.
# Once this is done, we make use of two pointers l and r pointing to the beginning and the end of the sorted list. 
# Then, we do as follows:
# 1. Check if the sum of the elements pointed by l and r is equal to the required sum kk. If so, return a True 
#    immediately.
# 2. Otherwise, if the sum of the current two elements is lesser than the required sum k, update l to point to the 
#    next element. This is done, because, we need to increase the sum of the current elements, which can only be 
#    done by increasing the smaller number.
# 3. Otherwise, if the sum of the current two elements is larger than the required sum k, update r to point to the 
#    previous element. This is done, because, we need to decrease the sum of the current elements, which can only 
#    be done by reducing the larger number.
# 4. Continue steps 1. to 3. till the left pointer l crosses the right pointer r.
# 5. If the two pointers cross each other, return a False value.
# Note that we need not increase the larger number or reduce the smaller number in any case. This happens because, 
# in case, a number larger than the current list[r] is needed to form the required sum k, the right pointer could 
# not have been reduced in the first place. The similar argument holds true for not reducing the smaller number as 
# well.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder(self, node, node_vals):
        if not node:
            return
        self.inorder(node.left, node_vals)
        node_vals.append(node.val)
        self.inorder(node.right, node_vals)
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        node_vals = []
        self.inorder(root, node_vals)
        
        l = 0
        r = len(node_vals) - 1
        
        while l < r:
            sum = node_vals[l] + node_vals[r]
            if sum == k:
                return True
            if sum < k:
                l += 1
            else:
                r -= 1
        
        return False
            
        
root = [5,3,6,2,4,None,7]
k = 9
obj = Solution()
print(obj.twoSum(root, k))


# Complexity Analysis:
# Time complexity : O(n). We need to traverse over the whole tree once to do the inorder traversal. Here, n refers 
# to the number of nodes in the given tree.
# Space complexity : O(n). The sorted list will contain n elements.
