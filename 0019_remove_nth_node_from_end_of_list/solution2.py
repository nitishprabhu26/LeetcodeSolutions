# https://youtu.be/XVuQxVej6y8

# Approach 2: One pass algorithm
# Algorithm:
# The previous algorithm could be optimized to one pass. Instead of one pointer, we could use two pointers. The first pointer advances
# the list by n+1 steps from the beginning, while the second pointer starts from the beginning of the list. Now, both pointers are
# exactly separated by n nodes apart. We maintain this constant gap by advancing both pointers together until the first pointer arrives
# past the last node. The second pointer will be pointing at the nth node counting from the last. We relink the next pointer of the
# node referenced by the second pointer to point to the node's next next node.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        first = dummy
        second = dummy

        # Advances first pointer so that the gap between first and second is n nodes apart
        for i in range(n + 1):
            first = first.next

        # Move first to the end, maintaining the gap
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next


head = [1, 2, 3, 4, 5]
n = 2
obj = Solution()
print(obj.removeNthFromEnd(head, n))

# Complexity Analysis:
# Time complexity : O(L).The algorithm makes one traversal of the list of L nodes. Therefore time complexity is O(L).
# Space complexity : O(1). We only used constant extra space.
