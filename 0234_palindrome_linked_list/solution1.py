# Approach 1: Copy into Array List and then Use Two Pointer Technique(for python - reverse list and compare)
# OR
# Neetcode: https://youtu.be/yOzXms1J6Nk

# Algorithm:
# Copying the Linked List into an Array.
# Checking whether or not the Array is a palindrome.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]
        

# OR

class Solution(object):
    def isPalindrome(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True 


head = [1,2,2,1]
obj = Solution()
print(obj.isPalindrome(head))


# Complexity analysis:
# Time complexity : O(n), where n is the number of nodes in the Linked List.
# Space complexity : O(n), where n is the number of nodes in the Linked List. We are making an Array List and 
# adding n values to it.