# Neetcode
# https://youtu.be/XVuQxVej6y8


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = dummy
        right = head

        # Advances right pointer so that the gap between right and left is n nodes apart
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move right to the end, maintaining the gap
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next


head = [1, 2, 3, 4, 5]
n = 2
obj = Solution()
print(obj.removeNthFromEnd(head, n))


# Complexity Analysis:
# Time complexity : O(L).
# The algorithm makes one traversal of the list of L nodes. Therefore time complexity is O(L).
# Space complexity : O(1). We only used constant extra space.
