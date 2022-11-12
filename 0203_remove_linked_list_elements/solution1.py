# Approach 1: Sentinel Node
# OR
# Neetcode: https://youtu.be/JI71sxtHTng

# Intuition:
# The problem seems to be very easy if one has to delete a node in the middle:
# - Pick the node-predecessor prev of the node to delete.
# - Set its next pointer to point to the node next to the one to delete.

# The things are more complicated when the node or nodes to delete are in the head of linked list.
# - We can achieve this with the help of sentinel node.(by reducing the problem to the deletion of middle nodes)
# Sentinel nodes are widely used in trees and linked lists as pseudo-heads, pseudo-tails, markers of level end, 
# etc. They are purely functional, and usually does not hold any data. Their main purpose is to standardize the 
# situation, for example, make linked list to be never empty and never headless and hence simplify insert and 
# delete.

# Algorithm:
# Initiate sentinel node as ListNode(0) and set it to be the new head: sentinel.next = head.
# Initiate two pointers to track the current node and its predecessor: curr and prev.
# While curr is not a null pointer:
# - Compare the value of the current node with the value to delete.
#   -   In the values are equal, delete the current node: prev.next = curr.next.
#   -   Otherwise, set predecessor to be equal to the current node.
# - Move to the next node: curr = curr.next.
# Return sentinel.next.


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(0)
        sentinel.next = head
        
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                # no need to update previous node, just update its next pointer
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return sentinel.next


# OR
# without using sentinel node: to handle the case where head node is equal to value
# https://youtu.be/gfFn-OXxcgU

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Case: where head node(or first few nodes is/are equal to cal; and are to be removed)
        # so we skip to the point where head node doesnt equal to val, and then set it as head node
        while head and head.val == val:
            head = head.next
            
        # Now head node is not equal to val
        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
                
        return head


head = [1,2,6,3,4,5,6]
val = 6
obj = Solution()
print(obj.removeElements(head, val))


# Complexity analysis:
# Time complexity : O(n), it's one pass solution.
# Space complexity : O(1), it's a constant space solution.