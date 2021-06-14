# Approach #2 (Recursive) 
# https://www.youtube.com/watch?v=bOOdi7S5Ar4
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

nums = [1,2,3,4,5]
obj = Solution()
print(obj.reverseList(nums))

# Complexity analysis:
# Time complexity : O(n). Assume that n is the list's length, the time complexity is O(n).
# Space complexity : O(n). The extra space comes from implicit stack space due to recursion. 
# The recursion could go up to n levels deep.