# Approach 1: Recursive Approach
# https://leetcode.com/problems/swap-nodes-in-pairs/solution/

# The basic intuition is to reach to the end of the linked list in steps of two using recursion. and while back 
# tracking, the nodes can be swapped.
# In every function call we take out two nodes which would be swapped and the remaining nodes are passed to the 
# next recursive call. The reason we are adopting a recursive approach here is because a sub-list of the original 
# list would still be a linked list and hence, it would adapt to our recursive strategy. Assuming the recursion 
# would return the swapped remaining list of nodes, we just swap the current two nodes and attach the remaining 
# list we get from recursion to these two swapped pairs.

# Algorithm:
# 1. Start the recursion with head node of the original linked list.
# 2. Every recursion call is responsible for swapping a pair of nodes. Let's represent the two nodes to be swapped 
#    by firstNode and secondNode.
# 3. Next recursion is made by calling the function with head of the next pair of nodes. This call would swap the 
#    next two nodes and make further recursive calls if there are nodes left in the linked list.
# 4. Once we get the pointer to the remaining swapped list from the recursion call, we can swap the firstNode and 
#    secondNode i.e. the nodes in the current recursive call and then return the pointer to the secondNode since 
#    it will be the new head after swapping.
# 5. Once all the pairs are swapped in the backtracking step, we would eventually be returning the pointer to the 
#    head of the now swapped list. This head will essentially be the second node in the original linked list.


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head
        
        # Nodes to be swapped
        first_node = head
        second_node = head.next
        
        # Swapping
        first_node.next  = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node


head = [1,2,3,4]
obj = Solution()
print(obj.swapPairs(head))


# Complexity Analysis:
# Time complexity : O(N) where N is the size of the linked list.
# Space complexity : O(N) stack space utilized for recursion.