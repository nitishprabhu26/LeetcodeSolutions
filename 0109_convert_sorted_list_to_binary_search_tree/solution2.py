# Approach 2: Recursion + Conversion to Array (approach is to use solution of 108)
# Convert the list into array, and convert this array into BST
# This approach is a classic example of the time-space tradeoff. You can get the time complexity down by using 
# more space.
# That's exactly what we're going to do in this approach. Essentially, we will convert the given linked list 
# into an array and then use that array to form our binary search tree. In an array fetching the middle 
# element is a O(1) operation and this will bring down the overall time complexity.

# Algorithm:
# - Convert the given linked list into an array. Let's call the beginning and the end of the array as left and 
#   right
# - Find the middle element as (left + right) / 2. Let's call this element as mid. This is a O(1) time operation 
#   and is the only major improvement over the previous algorithm.
# - The middle element forms the root of the BST.
# - Recursively form binary search trees on the two halves of the array represented by 
#   (left, mid - 1) and (mid + 1, right) respectively.


from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # Convert the given linked list to an array
    def mapListToValues(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals    

    def sortedListToBST(self, head):

        # Form an array out of the given linked list and then
        # use the array to form the BST.
        values = self.mapListToValues(head)

        # l and r represent the start and end of the given array
        def convertListToBST(l, r):

            # Invalid case
            if l > r:
                return None

            # Middle element forms the root.
            mid = (l + r) // 2
            node = TreeNode(values[mid])

            # Base case for when there is only one element left in the array
            if l == r:
                return node

            # Recursively form BST on the two halves
            node.left = convertListToBST(l, mid - 1)
            node.right = convertListToBST(mid + 1, r)
            return node
        return convertListToBST(0, len(values) - 1)



head = [-10,-3,0,5,9]
obj = Solution()
print(obj.sortedListToBST(head))


# Complexity Analysis:

# Time complexity : The time complexity comes down to just O(N) now since we convert the linked list to an 
# array initially and then we convert the array into a BST. Accessing the middle element now takes O(1) time 
# and hence the time complexity comes down.
# Space complexity :  Since we used extra space to bring down the time complexity, the space complexity now 
# goes up to O(N) as opposed to just O(logN) in the previous solution. This is due to the array we construct 
# initially.
