# Approach 2: Iteration
# https://leetcode.com/problems/merge-two-sorted-lists/solution/
# OR
# Neetcode
# https://youtu.be/XIdigk956u0

# Algorithm
# First, we set up a false "prehead" node that allows us to easily return the head of the merged list later. 
# We also maintain a prev pointer, which points to the current node for which we are considering adjusting 
# its next pointer. Then, we do the following until at least one of l1 and l2 points to null: 
# if the value at l1 is less than or equal to the value at l2, then we connect l1 to the previous node and 
# increment l1. Otherwise, we do the same, but for l2. Then, regardless of which list we connected, we 
# increment prev to keep it one step behind one of our list heads.
# After the loop terminates, at most one of l1 and l2 is non-null. Therefore (because the input lists were in 
# sorted order), if either list is non-null, it contains only elements greater than all of the 
# previously-merged elements. This means that we can simply connect the non-null list to the merged list and 
# return it.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)
        
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1=l1.next
            else:
                l1.val>=l2.val
                prev.next = l2
                l2=l2.next
            prev=prev.next
            
        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2
        
        return prehead.next


list1 = [1,2,4]
list2 = [1,3,4]
obj = Solution()
print(obj.mergeTwoLists(list1, list2))

# Complexity Analysis:
# Time complexity : O(n+m)
# Because exactly one of l1 and l2 is incremented on each loop iteration, the while loop runs for a number of 
# iterations equal to the sum of the lengths of the two lists. All other work is constant, so the overall 
# complexity is linear.
# Space complexity : O(1)
# The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.