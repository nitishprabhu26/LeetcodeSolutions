# Approach : Recursion

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def rec(node, val):
            if node:
                if node.val == val:
                    return rec(node.next, val)
                else:
                    node.next = rec(node.next, val)
                return node
        return rec(head, val)

head = [1,2,6,3,4,5,6]
val = 6
obj = Solution()
print(obj.removeElements(head, val))

# Complexity analysis:
# Time complexity : O(n).
# Space complexity : O(n).