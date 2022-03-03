# Approach 1:

# Intuition:
# The nodes in the list are already linked, and hence the rotation basically means:
# -   To close the linked list into the ring.
# -   To break the ring after the new tail and just in front of the new head.

# Algorithm:
# - Find the old tail and connect it with the head: old_tail.next = head to close the ring. Compute the length of 
#   the list n at the same time.
# - Find the new tail, which is (n - k % n - 1)th node from the head and the new head, which is (n - k % n)th node.
# - Break the ring new_tail.next = None and return new_head.


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base cases
        if not head:
            return None
        if not head.next:
            return head
        
        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head
        
        # find new tail : (n - k % n - 1)th node OR i.e.(n - (k % n) - 1)th node
        # and new head : (n - k % n)th node OR i.e.(n - (k % n))th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # break the ring
        new_tail.next = None
        
        return new_head
            

head = [1,2,3,4,5]
k = 2
obj = Solution()
print(obj.rotateRight(head, k))


# Complexity:
# Time Complexity: O(N), where N is a number of elements in the list.
# Space Complexity: O(1), since it's a constant space solution.