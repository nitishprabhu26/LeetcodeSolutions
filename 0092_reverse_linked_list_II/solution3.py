# Approach : Neetcode
# https://youtu.be/RF_M9tX4Eag


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # 1) reach node at position "left"
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        # Now cur="left", leftPrev="node before left"
        # 2) reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        # 3) Update pointers
        leftPrev.next.next = cur  # cur is node after "right"
        leftPrev.next = prev  # prev is "right"
        return dummy.next


head = [1,2,3,4,5]
left = 2
right = 4
obj = Solution()
print(obj.reverseBetween(head, left, right))


# Complexity Analysis:
# Time Complexity: O(N) considering the list consists of N nodes. We process each of the nodes at most once 
# (we don't process the nodes after the n^{th} node from the beginning.
# Space Complexity: O(1) since we simply adjust some pointers in the original linked list and only use O(1) 
# additional memory for achieving the final result.