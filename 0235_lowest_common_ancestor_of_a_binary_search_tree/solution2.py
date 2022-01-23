# Approach 1: Recursive Approach

# Intuition:
# Lowest common ancestor for two nodes p and q would be the last ancestor node common to both of them. Here 
# last is defined in terms of the depth of the node.

# Algorithm:
# 1. Start traversing the tree from the root node.
# 2. If both the nodes p and q are in the right subtree, then continue the search with right subtree starting 
# step 1.
# 3. If both the nodes p and q are in the left subtree, then continue the search with left subtree starting 
# step 1.
# 4. If both step 2 and step 3 are not true, this means we have found the node which is common to node p's 
# and q's subtrees. and hence we return this common node as the LCA.
# (step4 exp: 
# case 1: p and q are seperate subtrees from the current node split occurs here, 
# case 2: one of the node is eqaual to the curr node(root node), then that node has to be the LCA)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root


root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]
p = 2
q = 8
obj = Solution()
print(obj.lowestCommonAncestor(root, p, q))


# Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the BST. In the worst case we might be visiting
# all the nodes of the BST.(skewed tree) when all node only has one child and p,q are near the bottom.
# For a balanced BST, the time complexity may be O(log(n)) since we reduce the nodes to check by half after 
# each step.
# Space Complexity: O(N). This is because the maximum amount of space utilized by the recursion stack would
# be N since the height of a skewed BST could be N.
