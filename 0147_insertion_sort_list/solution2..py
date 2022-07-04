# Neetcode https://youtu.be/Kk6mXAzqX3Y


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = head, head.next
        
        while cur:
            # if its already in order - extra check
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                continue
            
            tmp = dummy
            while cur.val > tmp.next.val:
                tmp = tmp.next
                
            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next
            # no need to advance prev pointer since prev is pointing to cur already

        return dummy.next


head = [4,2,1,3]
obj = Solution()
print(obj.insertionSortList(head))


# Complexity analysis:
# Let N be the number of elements in the input list.
# Time complexity : O(N^2). worst case time complexity.
# O(N) - best case, if its already in sorted order. (possible since we check the cur element value with previous 
# element value; and if in order we skip the iteration code since its already in order - extra check)
# Space complexity: O(1). 
# We used some pointers within the algorithm. However, their memory consumption is constant regardless of the input.
# Note, we did not create new nodes to hold the values of input list, but simply reorder the existing nodes.