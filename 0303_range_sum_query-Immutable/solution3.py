# Approach 3: Caching [Accepted]

# The previous approach takes a lot of space, could we optimize it?
# Imagine that we pre-compute the cummulative sum from index 0 to k. Could we use this information to derive 
# Sum(i,j)?
# Let us define sum[k] as the cumulative sum for nums[0⋯k−1] (inclusive):
# sum[k] = { nums[0⋯k−1] , k > 0
#          { 0            , k = 0
# Now, we can calculate sumRange as following:
# sumRange(i, j) = sum[j + 1] - sum[i]


from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.sum[i + 1] = self.sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right + 1] - self.sum[left]


# Notice in the code above we inserted a dummy 0 as the first element in the sum array. This trick saves us from 
# an extra conditional check in sumRange function.


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
for left, right in [[0, 2], [2, 5], [0, 5]]:
    print(obj.sumRange(left, right))


# Complexity Analysis
# Time Complexity: O(1) time per query, O(n) time pre-computation. Since the cumulative sum is cached, each
# sumRange query can be calculated in O(1) time.
# Space Complexity : O(n).
