# Approach : Using extra space for a List to store node values.
# https://youtu.be/6qHflItkcg0


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        nodeList = []
        def inorder(node):
            if not node:
                return None
            
            inorder(node.left)
            nodeList.append(node)
            inorder(node.right)
            
            
        if not root:
            return None
        
        inorder(root)
        
        for i in range(len(nodeList) - 1):
            nodeList[i].right = nodeList[i + 1]
            nodeList[i].left = None
            
        nodeList[len(nodeList) - 1].left = None
        nodeList[len(nodeList) - 1].right = None
        
        return nodeList[0]


root = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
obj = Solution()
print(obj.increasingBST(root))


# Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the given tree.
# Space Complexity: O(N) to store values in a list, and also for recursion stack.
