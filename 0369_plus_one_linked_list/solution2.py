# Approach 1: Sentinel Head + Textbook Addition.
# https://leetcode.com/problems/plus-one-linked-list/solution/


# Algorithm:
# - Initialize sentinel node as ListNode(0) and set it to be the new head: sentinel.next = head.
# - Find the rightmost digit not equal to nine.
# - Increase that digit by one.
# - Set all the following nines to zero.
# - Return sentinel node if it was set to 1, and head sentinel.next otherwise.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # sentinel head
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel

        # find the rightmost not-nine digit
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        # increase this rightmost not-nine digit by 1
        not_nine.val += 1
        not_nine = not_nine.next

        # set all the following nines to zeros
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next

        return sentinel if sentinel.val else sentinel.next
    

# head = [1,2,3]
# obj = Solution()
# print(obj.plusOne(head))


# Complexity Analysis:
# Time complexity : O(N) since it's not more that two passes along the input list.
# Space complexity : O(1).