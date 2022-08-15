# Approach #1 Using HashSet[Accepted]
# OR
# https://youtu.be/AswWgktaeDk

# For every current node with a value of p, we check if k-p already exists in the array. If so, we can conclude 
# that the sum k can be formed by using the two elements from the given tree. Otherwise, we put this value p into 
# the setset.
# If even after the whole tree's traversal, no such element p can be found, the sum k can't be formed by using any 
# two elements.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hash_set = set()
        
        def dfs(node):
            if not node:
                return False
            
            y = k - node.val
            
            if y in hash_set:
                return True
            else:
                hash_set.add(node.val)
                return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
                    

root = [5,3,6,2,4,None,7]
k = 9
obj = Solution()
print(obj.findTarget(root, k))


# Complexity Analysis:
# Time complexity : O(n). The entire tree is traversed only once in the worst case. Here, nn refers to the number 
# of nodes in the given tree.
# Space complexity : O(n). The size of the set can grow upto n in the worst case.
