# Approach 1: Straight-Forward Approach
# OR
# Neetcode
# https://youtu.be/p10f-VpO4nE

# Intuition:
# Since the input list is sorted, we can determine if a node is a duplicate by comparing its value to the node 
# after it in the list. If it is a duplicate, we change the next pointer of the current node so that it skips the 
# next node and points directly to the one after the next node.

from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
                
        return head

head = [1,1,2]
obj = Solution()
print(obj.deleteDuplicates(head))


# Complexity Analysis:
# Time complexity : O(n). Because each node in the list is checked exactly once to determine if it is a duplicate 
# or not, the total run time is O(n), where n is the number of nodes in the list.
# Space complexity : O(1). No additional space is used.

