# Nested Loop approach - Neetcode
# https://youtu.be/p10f-VpO4nE

# Intuition:
# 2 loop approach: Nested loop
# outer loop - determines where our current pointer is
# inner loop - deletes the duplicate nodes
# So, even with nested loop time complexity is still O(n)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        while current:
            while current.next and current.next.val == current.val:
                current.next = current.next.next

            current = current.next
                
        return head

head = [1,1,2]
obj = Solution()
print(obj.deleteDuplicates(head))


# Complexity Analysis:
# Time complexity : O(n). Because each node in the list is checked exactly once to determine if it is a duplicate 
# or not, the total run time is O(n), where n is the number of nodes in the list.
# Space complexity : O(1). No additional space is used.

