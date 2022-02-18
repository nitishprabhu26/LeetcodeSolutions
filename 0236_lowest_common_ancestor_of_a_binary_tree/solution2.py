# Approach 1 : (Post order traversal - solution1.py is Post order traversal as well)
# https://youtu.be/9wWHSq0YDl8 (code)
# OR
# https://youtu.be/xuvw11Ucqs8 (to understand)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def dfs(node):
            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            # If the current node is one of p or q
            mid = node == p or node == q

            # If any two of the three flags left, right or mid become True.
            if (left and right) or (left and mid) or (right and mid):
                self.ans = node

            # Return True if either of the three bool values is True.
            return mid or left or right

        dfs(root)
        return self.ans


root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 1
obj = Solution()
print(obj.lowestCommonAncestor(root, p, q))


# Complexity Analysis:

# Time Complexity: O(N), where N is the number of nodes in the binary tree. In the worst case we might be visiting
# all the nodes of the binary tree.
# Space Complexity: O(N). This is because the maximum amount of space utilized by the recursion stack would be N
# since the height of a skewed binary tree could be N.
