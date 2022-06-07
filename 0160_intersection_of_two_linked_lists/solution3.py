# Approach 3: Two Pointers
# https://leetcode.com/problems/intersection-of-two-linked-lists/solution/

# Intuition:
# We know that we've now fully optimized the time complexity: it's impossible to do better than O(N + M) as, in 
# the worst case, we'll need to look at every node at least once. There is a way we can get the space complexity 
# down to O(1) while maintaining O(N + M) time complexity that we just achieved.
# Observe that while list A and list B could be different lengths, that the shared "tail" following the 
# intersection has to be the same length.

# We would start by setting a pointer at the start of the shorter list, and a pointer at the first possible 
# matching node of the longer list. The position of this node is simply the difference between the two lengths, 
# that is, |M - N|.
# Then, we just need to step the two pointers through the list, each time checking whether or not the nodes are 
# the same.
# In code, we could write this algorithm with 4 loops, one after the other, each doing the following:
# - Calculate N; the length of list A.
# - Calculate M; the length of list B.
# - Set the start pointer for the longer list.
# - Step the pointers through the list together.
# https://youtu.be/8qi8a2ph71o


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        tempA, tempB = headA, headB
        
        # Calculate the length of list A.
        while tempA is not None:
            lenA += 1
            tempA = tempA.next
            
        # Calculate the length of list B.
        while tempB is not None:
            lenB += 1
            tempB = tempB.next
        
        # Set the start pointer for the longer list.
        diff = abs(lenA - lenB)
        tempA, tempB = headA, headB
        
        print(diff)
        if lenA > lenB:
            while diff > 0:
                tempA = tempA.next
                diff -= 1
        else:
            while diff > 0:
                tempB = tempB.next
                diff -= 1
        
        # Step the pointers through the list together.
        while tempA is not tempB:
            tempA = tempA.next
            tempB = tempB.next
            if tempA is None or tempB is None:
                return None
        
        return tempA


# While this would have a time complexity of O(N + M) and a space complexity of O(1), we can still simplify.
# https://leetcode.com/problems/intersection-of-two-linked-lists/solution/
# OR
# Neetcode: https://youtu.be/D0X0BONOQhI

# If we say that c is the shared part, a is exclusive part of list A and b is exclusive part of list B, then we 
# can have one pointer that goes over a + c + b and the other that goes over b + c + a.(so that both pointer travel
# same distance) Have a look at the diagram.

# one pointer is essentially measuring the length of the longer list, and the other is measuring the length of the 
# shorter list, and then placing the start pointer for the longer list. Then both are stepping through the list 
# together.
# (The idea of resetting the pointers once it reaches the end works because it ensures that both pointers travels 
# the same distance, and eventually end up meeting at the same point)(works when there is no intersection as well)

# Algorithm:
# - Set pointer pA to point at headA.
# - Set pointer pB to point at headB.
# - While pA and pB are not pointing at the same node:
#       - If pA is pointing to a null, set pA to point to headB.
#       - Else, set pA to point at pA.next.
#       - If pB is pointing to a null, set pB to point to headA.
#       - Else, set pB to point at pB.next.
# - return the value pointed to by pA (or by pB; they're the same now).


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
        # Note: In the case lists do not intersect, the pointers for A and B
        # will still line up in the 2nd iteration, just that here won't be
        # a common node down the list and both will reach their respective ends
        # at the same time. So pA will be NULL in that case.


# OR
# Neetcode: https://youtu.be/D0X0BONOQhI


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1


# Complexity Analysis:
# Let N be the length of list A and M be the length of list B.
# Time Complexity : O(N + M).
# In the worst case, each list is traversed twice giving 2.M + 2.N, which is equivalent to O(N + M). This is 
# because the pointers firstly go down each list so that they can be "lined up" and then in the second iteration, 
# the intersection node is searched for.
# An interesting observation you might have made is that when the lists are of the same length, this algorithm 
# only traverses each list once. This is because the pointers are already "lined up" from the start, so the 
# additional pass is unnecessary.
# Space Complexity : O(1).
# We aren't allocating any additional data structures, so the amount of extra space used does not grow with the 
# size of the input. For this reason, Approach 3 is better than Approach 2.