# Approach 1: BFS (Breadth-First Search)

# Most intuitive solution would be the BFS (Breadth-First Search) approach through which we traverse the tree 
# level-by-level. The default ordering of BFS within a single level is from left to right. As a result, we should 
# adjust the BFS algorithm a bit to generate the desired zigzag ordering.
# One of the keys here is to store the values that are of the same level with the deque (double-ended queue) 
# data structure, where we could add new values on either end of a queue.

# So if we want to have the ordering of FIFO, we simply append the new elements to the tail of the queue. 
# While if we want to have the ordering of FILO, we insert the new elements to the head of the queue.

# Algorithm:

# There are several ways to implement the BFS algorithm:
# 1. One way would be that we run a two-level nested loop, with the outer loop iterating each level on the tree, 
# and with the inner loop iterating each node within a single level.
# 2. We could also implement BFS with a single loop though. The trick is that we append the nodes to be visited 
# into a queue and we separate nodes of different levels with a sort of delimiter (e.g. an empty node). The 
# delimiter marks the end of a level, as well as the beginning of a new level.

# Here we adopt the second approach above. One can start with the normal BFS algorithm, upon which we add a touch 
# of zigzag order with the help of deque. For each level, we start from an empty deque container to hold all the 
# values of the same level. Depending on the ordering of each level, i.e. either from-left-to-right or 
# from-right-to-left, we decide at which end of the deque to add the new element:
# - For the ordering of from-left-to-right (FIFO), we append the new element to the tail of the queue, so that the 
# element that comes late would get out late as well.
# - For the ordering of from-right-to-left (FILO), we insert the new element to the head of the queue, so that the 
# element that comes late would get out first.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        ret = []
        level_list = deque()
        if root is None:
            return []
        # start with the level 0 with a delimiter
        node_queue = deque([root, None])
        is_order_left = True
        
        while len(node_queue) > 0:
            curr_node = node_queue.popleft()

            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # we finish one level
                ret.append(level_list)
                # add a delimiter to mark the level
                if len(node_queue) > 0:
                    node_queue.append(None)

                # prepare for the next level
                level_list = deque()
                is_order_left = not is_order_left

        return ret

root = [3,9,20,None,None,15,7]
obj = Solution()
print(obj.zigzagLevelOrder(root))


# Complexity Analysis:

# Time complexity : O(N), where N is the number of nodes in the tree. 
# - We visit each node once and only once.
# - In addition, the insertion operation on either end of the deque takes a constant time, rather than using the 
# array/list data structure where the inserting at the head could take the O(K) time where K is the length of 
# the list.
# Space complexity : O(N) where N is the number of nodes in the tree.
# - The main memory consumption of the algorithm is the node_queue that we use for the loop, apart from the array 
# that we use to keep the final output.
# - As one can see, at any given moment, the node_queue would hold the nodes that are at most across two levels. 
# Therefore, at most, the size of the queue would be no more than 2⋅L, assuming L is the maximum number of nodes 
# that might reside on the same level. Since we have a binary tree, the level that contains the most nodes could 
# occur to consist all the leave nodes in a full binary tree, which is roughly L = N/2. 
# As a result, we have the space complexity of 2.(N/2) = N in the worst case.