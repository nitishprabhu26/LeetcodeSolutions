# Approach : Iterative solution
# https://leetcode.com/problems/trim-a-binary-search-tree/discuss/719550/Python%3A-iterative-version


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        # 1. Find the root:
        node = root
        while node is not None:
            if node.val > high:
                node = node.left
                
            elif node.val < low:
                node = node.right
            
            else:
                break
        root = node
        
        # for testcase: [3], 2, 2
        if root is None:
            return None
        
        # 2. Trim the left subtree
        parent = root
        node = root.left
        while node is not None:
            if node.val < low:
                parent.left = node.right
                node = node.right
                
            else:
                parent = node
                node = node.left
        parent.left = None
        
        # 3. Trim the right subtree:
        parent = root
        node = root.right
        while node is not None:
            if node.val > high:
                parent.right = node.left
                node = node.left
            
            else:
                parent = node
                node = node.right
        parent.right = None
        
        return root


root = [1,0,2]
low = 1
high = 2
obj = Solution()
print(obj.trimBST(root, low, high))


# Complexity Analysis:
# Time Complexity: O(N)
# Space Complexity: O(1)