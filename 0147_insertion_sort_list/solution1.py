# Approach 1: Insertion Sort

# Intuition:
# Let us first review the idea of insertion sort algorithm, which can be broke down into the following steps:
# - First of all, we create an empty list which would be used to hold the results of sorting.
# - We then iterate through each element in the input list. For each element, we need to find a proper position in 
#   the resulting list to insert the element, so that the order of the resulting list is maintained.
# - As one can see, once the iteration in the above step terminates, we will obtain the resulting list where the 
#   elements are ordered.

# Algorithm:
# To translate the above intuition into the implementation, we applied two tricks.
# - The first trick is that we will create a dummy (pseudo_head) node which serves as a pointer pointing to the 
#   resulting list.
# - In order to insert a new element into a singly-linked list, we apply another trick: The idea is that we use a 
#   pair of pointers (namely prev -> next) which serve as place-holders to guard the position where in-between we 
#   would insert a new element (i.e. prev -> new_node -> next).


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head

        while curr:
            # At each iteration, we insert an element into the resulting list.
            prev = dummy

            # find the position to insert the current node
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            next = curr.next
            # insert the current node to the new list
            curr.next = prev.next
            prev.next = curr

            # moving on to the next iteration
            curr = next

        return dummy.next


head = [4,2,1,3]
obj = Solution()
print(obj.insertionSortList(head))


# Complexity analysis:
# Let N be the number of elements in the input list.
# Time complexity : O(N^2).
# - First of all, we run an iteration over the input list.
# - At each iteration, we insert an element into the resulting list. In the worst case where the position to insert 
#   is the tail of the list, we have to walk through the entire resulting list.
# - As a result, the total steps that we need to walk in the worst case would be N(N+1)/2.
# Space complexity: O(1). 
# We used some pointers within the algorithm. However, their memory consumption is constant regardless of the input.
# Note, we did not create new nodes to hold the values of input list, but simply reorder the existing nodes.