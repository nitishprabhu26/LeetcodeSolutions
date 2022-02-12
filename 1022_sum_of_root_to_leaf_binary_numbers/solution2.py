# Approach 2: Recursive Preorder Traversal.

# Iterative approach 1 could be converted into recursive one.
# Recursive preorder traversal is extremely simple: follow Root->Left->Right direction, i.e. do all the business 
# with the node (= update the current number and root-to-leaf sum), and then do the recursive calls for the left 
# and right child nodes.

# Why non local?
# https://youtu.be/yLdGcj36Cww

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        root_to_leaf = 0
        def preorder(r, curr_number):
            nonlocal root_to_leaf
            if r:
                curr_number = (curr_number << 1) | r.val
                # if it's a leaf, update root-to-leaf sum
                if not (r.left or r.right):
                    root_to_leaf += curr_number
                    
                preorder(r.left, curr_number)
                preorder(r.right, curr_number) 
                
        preorder(root, 0)
        return root_to_leaf


root = [1,0,1,0,1,0,1]
obj = Solution()
print(obj.sumRootToLeaf(root))

# Complexity Analysis:
# Time complexity: O(N), where N is a number of nodes, since one has to visit each node.
# Space complexity: up to O(H) to keep the recursion stack, where H is a tree height.