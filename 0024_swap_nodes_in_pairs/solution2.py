# Approach 2: Iterative Approach
# https://leetcode.com/problems/swap-nodes-in-pairs/solution/

# Intuition
# The concept here is similar to the recursive approach. We break the linked list into pairs by jumping in steps 
# of two. The only difference is, unlike recursion, we swap the nodes on the go. After swapping a pair of nodes, 
# say A and B, we need to link the node B to the node that was right before A. To establish this linkage we save 
# the previous node of node A in prevNode.

# Algorithm:
# 1. We iterate the linked list with jumps in steps of two.
# 2. Swap the pair of nodes as we go, before we jump to the next pair. Let's represent the two nodes to be swapped 
#    by firstNode and secondNode.
# 3. Swap the two nodes. The swap step is
#       firstNode.next = secondNode.next
#       secondNode.next = firstNode
# 4. We also need to assign the prevNode's next to the head of the swapped pair. This step would ensure the 
#    currently swapped pair is linked correctly to the end of the previously swapped list.
#       prevNode.next = secondNode
# This is an iterative step, so the nodes are swapped on the go and attached to the previously swapped list. And 
# in the end we get the final swapped list.


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy
        
        while head and head.next:

            # Nodes to be swapped
            first_node = head
            second_node = head.next

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next


head = [1,2,3,4]
obj = Solution()
print(obj.swapPairs(head))


# Complexity Analysis:
# Time complexity : O(N) where N is the size of the linked list.
# Space complexity : O(1).