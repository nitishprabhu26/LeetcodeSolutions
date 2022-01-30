# Approach 1: Recursion
# https://leetcode.com/problems/merge-two-sorted-lists/solution/

# Algorithm:
# We model the above recurrence directly, first accounting for edge cases. Specifically, if either of l1 or l2
# is initially null, there is no merge to perform, so we simply return the non-null list. Otherwise, we
# determine which of l1 and l2 has a smaller head, and recursively set the next value for that head to the
# next merge result. Given that both lists are null-terminated, the recursion will eventually terminate.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


list1 = [1,2,4]
list2 = [1,3,4]
obj = Solution()
print(obj.mergeTwoLists(list1, list2))

# Complexity Analysis:
# Time complexity : O(n+m)
# Because each recursive call increments the pointer to l1 or l2 by one (approaching the dangling null at the 
# end of each list), there will be exactly one call to mergeTwoLists per element in each list. Therefore, the 
# time complexity is linear in the combined size of the lists.
# Space complexity : O(n+m)
# The first call to mergeTwoLists does not return until the ends of both l1 and l2 have been reached, so n+m 
# stack frames consume O(n+m) space.