# Neetcode solution
# https://youtu.be/wgFPrzTjm7s

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # new digit
            val = v1 + v2 + carry
            # in case of 'val=15'
            carry = val // 10
            val = val % 10
            
            cur.next = ListNode(val)
            
            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            # another edge case is 8+7=15, and carry here is 1. no other nodes in l1 or l2
            # so we add an or condition for carry in while
        
        return dummy.next



# alternative if no carry in while loop above

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # new digit
            val = v1 + v2 + carry
            # in case of 'val=15'
            carry = val // 10
            val = val % 10
            
            cur.next = ListNode(val)
            
            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            # another edge case is 8+7=15, and carry here is 1. no other nodes in l1 or l2
            # so we add an or condition for carry in while
            
        # alternative if no carry in while loop above
        if carry > 0:
            cur.next = ListNode(carry)
            
        return dummy.next



# Complexity Analysis:

# Time complexity : O(max(m,n)). Assume that m and n represents the length of l1 and l2 respectively, 
# the algorithm above iterates at most max(m,n) times.
# Space complexity : O(max(m,n)). The length of the new list is at most max(m,n)+1