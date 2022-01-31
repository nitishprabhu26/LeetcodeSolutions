# Approach 1: Reverse the Second Part of the List and Merge Two Sorted Lists
# OR
# Neetcode:
# https://youtu.be/S5bfdUTrKLM

# This problem is a combination of these three easy problems:
# - 0876. Middle of the Linked List.
# - 0206. Reverse Linked List.
# - 0021. Merge Two Sorted Lists.

# Overview:
# - Find a middle node of the linked list. If there are two middle nodes, return the second middle node. 
#   Example: for the list 1->2->3->4->5->6, the middle element is 4.
# - Once a middle node has been found, reverse the second part of the list. Example: convert 1->2->3->4->5->6 
#   into 1->2->3->4 and 6->5->4.
# - Now merge the two sorted lists. Example: merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 
        
        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next       

        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

head = [1,2,3,4]
obj = Solution()
print(obj.reorderList(head))

# Complexity analysis
# Time complexity : O(N). There are three steps here. To identify the middle node takes O(N) time. To reverse 
# the second part of the list, one needs N/2 operations. The final step, to merge two lists, requires N/2 
# operations as well. In total, that results in O(N) time complexity.
# Space complexity: O(1). since we do not allocate any additional data structures.