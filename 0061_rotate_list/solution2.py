# Approach : Neetcode
# https://youtu.be/UcGtPs2LE_c


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
            return head 
        
        # Get length
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        # move to the pivot and rotate
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        tail.next = head
        
        return new_head
            
            

head = [1,2,3,4,5]
k = 2
obj = Solution()
print(obj.rotateRight(head, k))


# Complexity:
# Time Complexity: O(N), where N is a number of elements in the list.
# Space Complexity: O(1), since it's a constant space solution.