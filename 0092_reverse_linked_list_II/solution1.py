# Approach 1: Recursion (modifying the values of the nodes for achieving the reversal)
# https://leetcode.com/problems/reverse-linked-list-ii/solution/


# Algorithm:
# 1. We define a recursion function that will do the job of reversing a portion of the linked list.
# 2. Let's call this function recurse. The function takes in 3 parameters: m being the starting point of the 
#    reversal, n being the ending point for the reversal, and a pointer right which will start at the n^{th} node 
#    in the linked list and move backwards with the backtracking of the recursion.
# 3. Additionally, we have a pointer called left which starts from the m^{th} node in the linked list and moves 
#    forward. In Python, we have to take a global variable for this which get's changed with recursion. In other 
#    languages, where changes made in function calls persist, we can consider this pointer as an additional 
#    variable for the function recurse.
# 4. In a recursion call, given m, n, and right, we check if n == 1. If this is the case, we don't need to go any 
#    further.
# 5. Until we reach n = 1, we keep moving the right pointer one step forward and after doing that, we make a 
#    recursive call with the value of n decreased by 1. At the same time, we keep on moving the left pointer 
#    forward until m == 1. When we refer to a pointer being moved forward, it essentially means pointer.next.
# 6. So we backtrack as soon as n reaches 1. At that point of time, the right pointer is at the last node of the 
#    sublist we want to reverse and the left has already reached the first node of this sublist. So, we swap out 
#    the data and move the left pointer one step forward using left = left.next. We need this change to persist 
#    across the backtracking process.
# 7. From there on, every time we backtrack, the right pointer moves one step backwards. The backward movement is 
#    simulated by backtracking.
# 8. We stop the swaps when either right == left, which happens if the sublist size is odd, or, right.next == left 
#    which happens when during the backtracking process for an even sized sublist, the right pointer crosses left. 
#    We use a global boolean flag for stopping the swaps once these conditions are met.


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:

        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers     
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next           

        recurseAndReverse(right, m, n)
        return head


head = [1,2,3,4,5]
left = 2
right = 4
obj = Solution()
print(obj.reverseBetween(head, left, right))


# Complexity Analysis:
# Time Complexity: O(N) since we process all the nodes at-most twice. Once during the normal recursion process and 
# once during the backtracking process. During the backtracking process we only just swap half of the list if you 
# think about it, but the overall complexity is O(N).
# Space Complexity: O(N) in the worst case when we have to reverse the entire list. This is the space occupied by 
# the recursion stack.