# Approach 2: Iterative using parent pointers

# Intuition:
# If we have parent pointers for each node we can traverse back from p and q to get their ancestors. The first 
# common node we get during this traversal would be the LCA node. We can save the parent pointers in a dictionary 
# as we traverse the tree.

# Algorithm:
# 1. Start from the root node and traverse the tree.
# 2. Until we find p and q both, keep storing the parent pointers in a dictionary.
# 3. Once we have found both p and q, we get all the ancestors for p using the parent dictionary and add to a 
# set called ancestors.
# 4. Similarly, we traverse through ancestors for node q. If the ancestor is present in the ancestors set for p, 
# this means this is the first ancestor common between p and q (while traversing upwards) and hence this is the 
# LCA node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}
        
        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q


root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 1
obj = Solution()
print(obj.lowestCommonAncestor(root, p, q))


# Complexity Analysis:

# Time Complexity: O(N), where N is the number of nodes in the binary tree. In the worst case we might be visiting
# all the nodes of the binary tree.
# Space Complexity: O(N). In the worst case space utilized by the stack, the parent pointer dictionary and the 
# ancestor set, would be N each, since the height of a skewed binary tree could be N.