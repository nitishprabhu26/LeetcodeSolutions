# Approach #1 (Iterative)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev_node = None
#         curr_node = head
#         while curr_node:
#             next_node = curr_node.next # Remember next node
#             curr_node.next = prev_node  # REVERSE! None, first time round.
#             prev_node = curr_node  # Used in the next iteration.
#             curr_node = next_node  # Move to next node.
#         head = prev_node
#         return head

nums = [1,2,3,4,5]
obj = Solution()
print(obj.reverseList(nums))

# Complexity analysis:
# Time complexity : O(n). Assume that n is the list's length, the time complexity is O(n).
# Space complexity : O(1).