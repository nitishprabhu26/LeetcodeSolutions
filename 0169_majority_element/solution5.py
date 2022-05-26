# Approach 5: Divide and Conquer

# Intuition:
# If we know the majority element in the left and right halves of an array, we can determine which is the global 
# majority element in linear time.

# Algorithm:
# Here, we apply a classical divide & conquer approach that recurses on the left and right halves of an array 
# until an answer can be trivially achieved for a length-1 array.
# In this case, the majority element for a length-1 slice is trivially its only element, so the recursion stops 
# there. If the current slice is longer than length-1, we must combine the answers for the slice's left and right 
# halves. If they agree on the majority element, then the majority element for the overall slice is obviously the 
# same. If they disagree, only one of them can be "correct", so we need to count the occurrences of the left and 
# right majority elements to determine which subslice's answer is globally correct. The overall answer for the 
# array is thus the majority element between indices 0 and n.


from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)
        

nums = [2,2,1,1,1,2,2]
obj = Solution()
print(obj.majorityElement(nums))


# Complexity Analysis:
# Time Complexity:  O(n.log n).
# Space Complexity: O(log n). Uses a non-constant amount of additional memory in stack frames due to recursion.