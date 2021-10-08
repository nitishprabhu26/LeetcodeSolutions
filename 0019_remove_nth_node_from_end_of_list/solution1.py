# https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/

# Approach 1: Two pass algorithm
# We notice that the problem could be simply reduced to another one : Remove the (L−n+1)th node from the beginning in the list ,
# where L is the list length. This problem is easy to solve once we found list length L.

# Algorithm:
# First we will add an auxiliary "dummy" node, which points to the list head. The "dummy" node is used to simplify some corner cases
# such as a list with only one node, or removing the head of the list. On the first pass, we find the list length L.
# Then we set a pointer to the dummy node and start to move it through the list till it comes to the (L−n)th node.
# We relink next pointer of the (L−n)th node to the (L−n+2)th node and we are done.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head

        # finding length of linked list
        while first:
            length += 1
            first = first.next

        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next

        first.next = first.next.next
        return dummy.next


head = [1, 2, 3, 4, 5]
n = 2
obj = Solution()
print(obj.removeNthFromEnd(head, n))

# Complexity Analysis:
# Time complexity : O(L).
# The algorithm makes two traversal of the list, first to calculate list length L and second to find the (L - n)th node.
# There are 2L−n operations and time complexity is O(L).
# Space complexity : O(1).
# We only used constant extra space.
