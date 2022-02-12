# Prerequisites: Bitwise Trick
# If you work with decimal representation, the conversion of 1->2 into 12 is easy. You start from curr_number = 1, 
# then shift one register to the left and add the next digit: curr_number = 1 * 10 + 2 = 12.
# If you work with binaries 1 -> 1 into 3, it's the same. You start from curr_number = 1, then shift one register 
# to the left and add the next digit: 
# curr_number = (1 << 1) | 1 = 3.
# or
# curr_number = (1 * 2) + 1 = 3.

# Prerequisites: Tree Traversals
# There are three DFS ways to traverse the tree: preorder, postorder and inorder. 

# Optimal Strategy to Solve the Problem:
# Root-to-left traversal is so-called DFS preorder traversal. To implement it, one has to follow straightforward 
# strategy Root->Left->Right.
# Since one has to visit all nodes, the best possible time complexity here is linear. Hence all interest here is 
# to improve the space complexity.

# There are 3 ways to implement preorder traversal: iterative, recursive and Morris.
# Iterative and recursive approaches here do the job in one pass, but they both need up to O(H) space to keep the 
# stack, where H is a tree height.
# Morris approach is two-pass approach, but it's a constant-space one.


# Approach 1: Iterative Preorder Traversal.

# Intuition:
# Here we implement standard iterative preorder traversal with the stack:
# Push root into stack.
# While stack is not empty:
    # - Pop out a node from stack and update the current number.
    # - If the node is a leaf, update root-to-leaf sum.
    # - Push right and left child nodes into stack.
# Return root-to-leaf sum.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        root_to_leaf = 0
        stack = [(root, 0) ]
        
        while stack:
            root, curr_number = stack.pop()
            if root is not None:
                curr_number = (curr_number << 1) | root.val
                # if it's a leaf, update root-to-leaf sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))
                        
        return root_to_leaf


root = [1,0,1,0,1,0,1]
obj = Solution()
print(obj.sumRootToLeaf(root))

# Complexity Analysis:
# Time complexity: O(N), where N is a number of nodes, since one has to visit each node.
# Space complexity: up to O(H) to keep the stack, where H is a tree height.