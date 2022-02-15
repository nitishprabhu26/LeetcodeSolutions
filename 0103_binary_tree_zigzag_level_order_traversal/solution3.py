# Approach 2: DFS (Depth-First Search)

# Intuition:
# We could also obtain the BFS traversal ordering via the DFS (Depth-First Search) traversal in the tree.
# The trick is that during the DFS traversal, we maintain the results in a global array that is indexed by the 
# level, i.e. the element array[level] would contain all the nodes that are at the same level. The global array 
# would then be referred and updated at each step of DFS.

# Algorithm
# Here we implement the DFS algorithm via recursion. We define a recursive function called DFS(node, level) which 
# only takes care of the current node which is located at the specified level. Within the function, here are 
# three steps that we would perform:
# - If this is the first time that we visit any node at the level, i.e. the deque for the level does not exist, 
# then we simply create the deque with the current node value as the initial element.
# - If the deque for this level exists, then depending on the ordering, we insert the current node value either 
# to the head or to the tail of the queue.
# - At the end, we recursively call the function for each of its child nodes.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        results = []
        def dfs(node, level):
            if level >= len(results):
                results.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node is not None:
                    dfs(next_node, level+1)

        # normal level order traversal with DFS
        dfs(root, 0)

        return results


root = [3,9,20,None,None,15,7]
obj = Solution()
print(obj.zigzagLevelOrder(root))


# Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the tree.
# Same as the previous BFS approach, we visit each node once and only once.
# Space Complexity: O(H), where H is the height of the tree, i.e. the number of levels in the tree, which would be 
# roughly log_2{N}.
# Unlike the BFS approach, in the DFS approach, we do not need to maintain the node_queue data structure for the 
# traversal.
# However, the function recursion would incur additional memory consumption on the function call stack. As we can 
# see, the size of the call stack for any invocation of DFS(node, level) would be exactly the number of level 
# that the current node resides on. Therefore, the space complexity of our DFS algorithm is O(log_2{N}) which is 
# much better than the BFS approach.