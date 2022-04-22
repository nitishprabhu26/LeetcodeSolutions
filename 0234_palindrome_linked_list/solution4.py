# Neetcode: https://youtu.be/yOzXms1J6Nk (Reverse Second Half In-place)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        fast = head
        slow = head
        
        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
        # check if palindrome
        left, right = head, prev
        # since we did: prev = None above
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


head = [1,2,2,1]
obj = Solution()
print(obj.isPalindrome(head))


# Complexity analysis:
# Time complexity : O(n), where n is the number of nodes in the Linked List.
# Space complexity : O(1). 
# We are changing the next pointers for half of the nodes. This was all memory that had already been allocated, so 
# we are not using any extra memory and therefore it is O(1).