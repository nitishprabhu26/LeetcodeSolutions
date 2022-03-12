# Approach : Neetcode (Iterative)
# https://youtu.be/o811TZLAWOo


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        # we need to have atleast 2 nodes to reverse, else break loop
        while curr and curr.next:

            # save ptrs
            nextPair = curr.next.next
            second = curr.next

            # reverse this pair
            second.next = curr
            curr.next = nextPair
            prev.next = second
            

            # update ptrs
            prev = curr
            curr = nextPair

        # Return the new head node.
        return dummy.next


head = [1,2,3,4]
obj = Solution()
print(obj.swapPairs(head))


# Complexity Analysis:
# Time complexity : O(N) where N is the size of the linked list.
# Space complexity : O(1).