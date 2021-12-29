# Neetcode https://youtu.be/gBTe7lFR3vc
# Floyd's Tortoise and Hare

# Algorithm
# Have 2 poineters, slow pointer 's' and fast pointer 'f'
# Originally they start at the same position
# Each time the slow pointer is shifted by '1' whereas the fast pointer is shifted by '2'
# if theres a null at end of linkedlist then fast pointer is going to reach there first
# else if cycle
# 'f' and 's' are going to meet again
# eg: explained in video
# on each iteration s moves by 1 and f moves by 2, 
# if gap between s and f is 10,
# then 10 - 1(slow) + 2(fast)
# = 9 (distance closed by 1 every iteration)
# gap could possibly be entire length of the linkedlist (time complexity) i.e. to bring 10 down to 0

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False

head = [3,2,0,-4]
obj = Solution()
print(obj.hasCycle(head))

# Complexity analysis
# Let n be the total number of nodes in the linked list.
# Time complexity : O(n). gap could possibly be entire length of the linkedlist. i.e. to bring 10 down to 0.
# Space complexity: O(1). We only use two nodes (slow and fast) 