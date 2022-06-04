# Approach 2: Caching [Accepted][Memory Limit Exceeded]

# Imagine that sumRange is called one thousand times with the exact same arguments. How could we speed that up?
# We could trade in extra space for speed. By pre-computing all range sum possibilities and store its results in 
# a hash table, we can speed up the query to constant time.


from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.dict = {}
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                self.dict[(i, j)] = sum

    def sumRange(self, left: int, right: int) -> int:
        return self.dict[(left, right)]


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
for left, right in [[0, 2], [2, 5], [0, 5]]:
    print(obj.sumRange(left, right))


# Complexity Analysis
# Time Complexity: O(1) time per query, O(n^2) time pre-computation. The pre-computation done in the constructor 
# takes O(n^2) time. Each sumRange query's time complexity is O(1) as the hash table's look up operation is 
# constant time.
# Space Complexity : O(n^2). The extra space required is O(n^2) as there are n candidates for both i and j.