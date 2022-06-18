# https://leetcode.com/problems/odd-even-linked-list/solution/
# OR
# https://youtu.be/C_LA6SOwVTM

# Intuition:
# Put the odd nodes in a linked list and the even nodes in another. Then link the evenList to the tail of the 
# oddList.

# Algorithm:
# A well-formed LinkedList need two pointers head and tail to support operations at both ends. The variables head 
# and odd are the head pointer and tail pointer of one LinkedList we call oddList; the variables evenHead and even 
# are the head pointer and tail pointer of another LinkedList we call evenList. The algorithm traverses the 
# original LinkedList and put the odd nodes into the oddList and the even nodes into the evenList. To traverse a 
# LinkedList we need at least one pointer as an iterator for the current node. But here the pointers odd and even 
# not only serve as the tail pointers but also act as the iterators of the original list.


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        # 'odd' and 'even' pointers will be at the end of oddList and evenList respectively
        odd = head
        even = head.next
        evenHead = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = evenHead
        return head


# example:
# head = [1,2,3,4,5]
# Output: [1,3,5,2,4]


# Complexity analysis:
# Time complexity : O(n). There are total n nodes and we visit each node once.
# Space complexity : O(1). All we need is the four pointers.
