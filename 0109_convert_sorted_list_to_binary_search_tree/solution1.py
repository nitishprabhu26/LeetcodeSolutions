# Approach 1: Recursion
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/solution/
# OR
# https://youtu.be/5IQF13nNq6A


# Algorithm:
# - Since we are given a linked list and not an array, we don't really have access to the elements of the list 
#   using indexes. We want to know the middle element of the linked list.
# - We can use the two pointer approach for finding out the middle element of a linked list. Essentially, we 
#   have two pointers called slow_ptr and fast_ptr. The slow_ptr moves one node at a time whereas the fast_ptr 
#   moves two nodes at a time. By the time the fast_ptr reaches the end of the linked list, the slow_ptr would 
#   have reached the middle element of the linked list. For an even sized list, any of the two middle elements 
#   can act as the root of the BST.
# - Once we have the middle element of the linked list, we disconnect the portion of the list to the left of 
#   the middle element. The way we do this is by keeping a prev_ptr as well which points to one node before 
#   the slow_ptr i.e. prev_ptr.next = slow_ptr. For disconnecting the left portion we simply do 
#   prev_ptr.next = None
# - We only need to pass the head of the linked list to the function that converts it to a height balances BST. 
#   So, we recurse on the left half of the linked list by passing the original head of the list and on the 
#   right half by passing slow_ptr.next as the head.


from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def findMiddle(self, head):

        # The pointer used to disconnect the left half from the mid node.
        prevPtr = None
        slowPtr = head
        fastPtr = head

        # Iterate until fastPr doesn't reach the end of the linked list.
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        # Handling the case when slowPtr was equal to head. (checking if prevPtr is not none)
        if prevPtr:
            prevPtr.next = None

        return slowPtr


    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # If the head doesn't exist, then the linked list is empty
        if not head:
            return None

        # Find the middle element for the list.
        mid = self.findMiddle(head)

        # The mid becomes the root of the BST.
        node = TreeNode(mid.val)

        # Base case when there is just one element in the linked list
        if head == mid:
            return node

        # Recursively form balanced BSTs using the left and right halves of the original list.
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node


head = [-10,-3,0,5,9]
obj = Solution()
print(obj.sortedListToBST(head))


# Complexity Analysis:

# Time Complexity: O(NlogN). Suppose our linked list consists of N elements. For every list we pass to our 
# recursive function, we have to calculate the middle element for that list. For a list of size N, it takes 
# N/2 steps to find the middle element i.e. O(N) to find the mid. We do this for every half of the original 
# linked list. From the looks of it, this seems to be an O(N^2) algorithm. However, on closer analysis, it 
# turns out to be a bit more efficient than O(N^2).
# Space complexity : O(logN).Since we are resorting to recursion, there is always the added space complexity 
# of the recursion stack that comes into picture. This could have been O(N) for a skewed tree, but the 
# question clearly states that we need to maintain the height balanced property. This ensures the height of 
# the tree to be bounded by O(logN). Hence, the space complexity is O(logN).
