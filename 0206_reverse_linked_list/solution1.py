# Approach #1 (Iterative)
# OR
# Neetcode: https://youtu.be/G0_I-ZF0S38

# Intuition:
# While traversing the list, we can change the current node's next pointer to point to its previous element. 
# Since a node does not have reference to its previous node, we must store its previous element beforehand. We 
# also need another pointer to store the next node before changing the reference. Do not forget to return the 
# new head reference at the end!


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev


# OR

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next # Remember next node
            curr.next = prev  # REVERSE! None, first time round.
            prev = curr  # Used in the next iteration.
            curr = next_node  # Move to next node.
            
        return prev


nums = [1,2,3,4,5]
obj = Solution()
print(obj.reverseList(nums))


# Complexity analysis:
# Time complexity : O(n). Assume that n is the list's length, the time complexity is O(n).
# Space complexity : O(1).