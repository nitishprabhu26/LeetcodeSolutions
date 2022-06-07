# Approach 1: Brute Force [Time Limit Exceeded]
# https://leetcode.com/problems/intersection-of-two-linked-lists/solution/

# Intuition and Algorithm
# For each node in list A, traverse over list B and check whether or not the node is present in list B.
# The one thing we need to be careful of is that we're comparing objects of type Node. We don't want to compare 
# the values within the nodes; doing this would cause our code to break when two different nodes have the same 
# value.


from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        while headA is not None:
            pB = headB
            while pB is not None:
                if headA == pB:
                    return headA
                pB = pB.next
            headA = headA.next
        return None



# Complexity Analysis:
# Let N be the length of list A and M be the length of list B.
# Time Complexity : O(N × M).
# For each of the N nodes in list A, we are traversing over each of the nodes in list B. In the worst case, we 
# won't find a match, and so will need to do this until reaching the end of list B, giving a worst-case time 
# complexity of O(N × M).
# Space Complexity : O(1).
# We aren't allocating any additional data structures, so the amount of extra space used does not grow with the 
# size of the input.