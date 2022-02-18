# Approach 1: Recursive Approach

# Intuition:
# Traverse the tree in a depth first manner. The moment you encounter either of the nodes p or q, return some 
# boolean flag. The flag helps to determine if we found the required nodes in any of the paths. The least common 
# ancestor would then be the node for which both the subtree recursions return a True flag. It can also be the 
# node which itself is one of p or q and for which one of the subtree recursions returns a True flag.

# Algorithm:
# 1. Start traversing the tree from the root node.
# 2. If the current node itself is one of p or q, we would mark a variable mid as True and continue the search for 
# the other node in the left and right branches.
# 3. If either of the left or the right branch returns True, this means one of the two nodes was found below.
# 4. If at any point in the traversal, any two of the three flags left, right or mid become True, this means we 
# have found the lowest common ancestor for the nodes p and q.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        # OR defining a local variable
        # ans = None
        
        def recurse_tree(current_node):
            # uncomment the below line to define variable
            # nonlocal ans
            
            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node
                # OR
                # ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans
        # OR
        # return ans



root = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 1
obj = Solution()
print(obj.lowestCommonAncestor(root, p, q))


# Complexity Analysis:

# Time Complexity: O(N), where N is the number of nodes in the binary tree. In the worst case we might be visiting 
# all the nodes of the binary tree. (skewed tree) 
# Space Complexity: O(N). This is because the maximum amount of space utilized by the recursion stack would be N
# since the height of a skewed binary tree could be N.