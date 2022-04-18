# Approach : Iterative with stack(extra space)
# https://youtu.be/vABwsgqI-_4?t=200


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        if not root:
            return None
        
        dummy = curr = TreeNode()
        stack = []
        
        while stack or root:
            # add to stack until the last leftmost value
            while root:
                stack.append(root)
                root = root.left
            
            # pop from stack and build new tree
            root = stack.pop()
            curr.right = root
            
            curr = curr.right
            root = root.right
            
            # without this we might end up with a cycle in the tree
            curr.left = None
            
        return dummy.right



root = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
obj = Solution()
print(obj.increasingBST(root))


# Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the given tree.
# Space Complexity: O(H) in additional space complexity, where H is the height of the given tree.
