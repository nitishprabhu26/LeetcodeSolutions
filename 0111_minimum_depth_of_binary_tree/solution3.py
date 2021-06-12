# Approach 3: BFS Iteration
# The drawback of the DFS approach in this case is that all nodes should be visited to ensure that the minimum depth would be found. Therefore, this results in a O(N) complexity. One way to optimize the complexity is to use the BFS strategy. We iterate the tree level by level, and the first leaf we reach corresponds to the minimum depth. As a result, we do not need to iterate all nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            node_deque = deque([(1, root),])
        
        while node_deque:
            depth, root = node_deque.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth + 1, c))

# obj = Solution()
# print(obj.levelOrder(root))


# Complexity Analysis:

# Time complexity :  in the worst case for a balanced tree we need to visit all nodes level by level up to the tree height, that excludes the bottom level only. This way we visit N/2N/2 nodes, and thus the time complexity is O(N).
# Space complexity : is the same as time complexity here O(N)
