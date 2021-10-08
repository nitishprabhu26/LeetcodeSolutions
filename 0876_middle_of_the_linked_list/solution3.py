# Approach 2: Fast and Slow Pointer
# When traversing the list with a pointer slow, make another pointer fast that traverses twice as fast. 
# When fast reaches the end of the list, slow must be in the middle.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


head = [1, 2, 3, 4, 5]
obj = Solution()
print(obj.middleNode(head))

# Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the given list.
# Space Complexity: O(1), the space used by slow and fast.
