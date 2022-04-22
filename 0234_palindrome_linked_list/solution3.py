# Approach 3: Reverse Second Half In-place

# Intuition:
# The only way we can avoid using O(n) extra space is by modifying the input in-place.
# The strategy we can use is to reverse the second half of the Linked List in-place (modifying the Linked List 
# structure), and then comparing it with the first half. Afterwards, we should re-reverse the second half and put 
# the list back together. While you don't need to restore the list to pass the test cases, it is still good 
# programming practice because the function could be a part of a bigger program that doesn't want the Linked List 
# broken.

# Algorithm:
# Specifically, the steps we need to do are:
# 1.Find the end of the first half - using two runners pointer technique.
# 2.Reverse the second half.
# 3.Determine whether or not there is a palindrome.
# 4.Restore the list.
# 5.Return the result.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result    

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
        

head = [1,2,2,1]
obj = Solution()
print(obj.isPalindrome(head))


# Complexity analysis:
# Time complexity : O(n), where n is the number of nodes in the Linked List.
# Similar to the above approaches. Finding the middle is O(n), reversing a list in place is O(n), and then 
# comparing the 2 resulting Linked Lists is also O(n).
# Space complexity : O(1). 
# We are changing the next pointers for half of the nodes. This was all memory that had already been allocated, so 
# we are not using any extra memory and therefore it is O(1).