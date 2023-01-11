# Approach 4: Counting Sort

# We can leverage the fact that the input number range is limited to [1..1000] and use a counting sort. Then, we 
# can use the two pointers pattern to enumerate pairs in the [1..1000] range.
# Note that the result can be a sum of two identical numbers, and that means that lo can be equal to hi. In this 
# case, we need to check if the count for that number is greater than one.

# Algorithm:
# - Count each element using the array count.
# - Set the lo number to zero, and hi to 1000.
# - While lo is smaller than, or equals hi:
#   -   If lo + hi is greater than k, or count[hi] == 0:
#       -   Decrement hi.
#   -   Else:
#       -   If count[lo] is greater than 0 (when lo < hi), or 1 (when lo == hi):
#           -   Track maximum lo + hi in the result answer.
#       -   Increment lo.
# - Return the result answer.


from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        answer = -1
        count = [0] * 1001
        for num in nums:
            count[num] += 1
        lo = 1
        hi = 1000
        while lo <= hi:
            if lo + hi >= k or count[hi] == 0:
                hi -= 1
            else:
                if count[lo] > (0 if lo < hi else 1):
                    answer = max(answer, lo + hi)
                lo += 1
        return answer


nums = [34,23,1,24,75,33,54,8]
k = 60
obj = Solution()
print(obj.twoSumLessThanK(nums, k))


# Optimizations:
# 1. We can set hi to either maximum number, or k - 1, whichever is smaller.
# 2. We can ignore numbers greater than k - 1.
# 3. We can use a boolean array (e.g. seen) instead of count. In the first loop, we will check if i is a 
#    duplicate (seen[i] is already true) and set answer to the highest i + i < k. Note that the two pointers loop 
#    will run while lo < hi, not while lo <= hi.
# 4. We can break from the two pointers loop as soon as nums[lo] > k / 2.


# Complexity analysis:
# Time Complexity: O(n + m), where m corresponds to the range of values in the input array.
# Space Complexity: O(m) to count each value.
