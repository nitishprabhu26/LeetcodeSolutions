# Approach 1: Top Down Merge Sort
# https://leetcode.com/problems/sort-list/solution/
# OR
# Neetcode: https://youtu.be/TGveA1oFhrc

# Intuition:
# Merge sort is a popularly known algorithm that follows the Divide and Conquer Strategy. The divide and conquer 
# strategy can be split into 2 phases:
# Divide phase: Divide the problem into subproblems.
# Conquer phase: Repeatedly solve each subproblem independently and combine the result to form the original problem.
# The Top Down approach for merge sort recursively splits the original list into sublists of equal sizes, sorts 
# each sublist independently, and eventually merge the sorted lists.

# Algorithm:
# - Recursively split the original list into two halves. The split continues until there is only one node in the 
#   linked list (Divide phase). To split the list into two halves, we find the middle of the linked list using the 
#   Fast and Slow pointer approach as mentioned in problem: 876.Find Middle Of Linked List.
# - Recursively sort each sublist and combine it into a single sorted list. (Merge Phase). This is similar to the 
#   problem: 21.Merge two sorted linked lists


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case: if head node is null or if list contains only one node
        if not head or not head.next:
            return head
        
        # split the lists in to 2 halfs
        left = head
        right = self.getMid(head)
        
        # we set right.next to be the right list, 
        # also break the list at the middle
        tmp = right.next
        right.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    
    def getMid(self, head):
        # using slow and fast pointer
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
            
        return dummy.next


# head = [4,2,1,3]
# obj = Solution()
# print(obj.sortList(head))


# Complexity analysis:
# Time complexity : O(nlogn), where n is the number of nodes in linked list. The algorithm can be split into 2 
# phases, Split and Merge.
# - Split:
#   The recursion tree expands in form of a complete binary tree, splitting the list into two halves recursively. 
#   The number of levels in a complete binary tree is given by O(log n).(number of times/levels we have to split 
#   our list to get each nodes seperated).
# - Merge:
#   Similar to split, we take O(log n). (number of times/levels we have to merge our list to get all nodes merged)
#   Taking 2 lists and merging them together, if already sorted is an O(n) operation.
#   So the time complexity for split and merge operation is O(n.log n).
# Space complexity: O(log n) , where n is the number of nodes in linked list. Since the problem is recursive, we 
# need additional space to store the recursive call stack. The maximum depth of the recursion tree is logn.