# Linear Solution: convert to int and back to linkedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        # convert linkedList to string -> to integer -> add one
        digits_str = ""
        while head:
            digits_str += str(head.val)
            head = head.next
            
        digits_int = int(digits_str) + 1
        
        # -> back to string
        digits_str = str(digits_int)
        
        # -> convert back to linkedList
        dummy = ListNode(0)
        newHead = dummy
        
        for digit in digits_str:
            newHead.next = ListNode(int(digit))
            newHead = newHead.next
            
        return dummy.next
    

# head = [1,2,3]
# obj = Solution()
# print(obj.plusOne(head))


# Complexity Analysis:
# Time complexity : O(N) since it's not more that two passes along the input list.
# Space complexity : O(N). space for newHead/dummy.