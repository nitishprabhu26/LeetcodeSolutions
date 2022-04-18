# Approach 2: Traversal with Relinking

# Intuition:
# The definition of a binary search tree is that for every node, all the values of the left branch are less than
# the value at the root, and all the values of the right branch are greater than the value at the root.
# Because of this, an in-order traversal of the nodes will yield all the values in increasing order.

# Algorithm:
# During the traversal, we'll construct the answer on the fly, reusing the nodes of the given tree by cutting 
# their left child and adjoining them to the answer.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right


root = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
obj = Solution()
print(obj.increasingBST(root))


# Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the given tree.
# Space Complexity: O(H) in additional space complexity, where H is the height of the given tree, and the size of 
# the implicit call stack in our in-order traversal.
