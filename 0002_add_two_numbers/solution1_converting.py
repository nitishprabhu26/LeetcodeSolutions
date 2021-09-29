# Not advisable. Here we are traversing both the linkedlists, converting them into
# the values for which we need to find the sum, now sum them and then later convert
# back the sum to linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ""
        num2 = ""
        while l1:
            num1 = str(l1.val)+num1
            l1 = l1.next
        while l2:
            num2 = str(l2.val)+num2
            l2 = l2.next
        out = str(int(num1)+int(num2))[::-1]
        result = ListNode(0)
        result_tail = result
        print(result)
        for i in out:
            result_tail.next = ListNode(i)
            result_tail = result_tail.next
        return result.next


l1 = [2, 4, 3]
l2 = [5, 6, 4]
obj = Solution()
print(obj.addTwoNumbers(l1, l2))
