# Approach 1: Brute Force [Time Limit Exceeded]

# Each time sumRange is called, we use a for loop to sum each individual element from index i to j.


from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.data = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for k in range(left, right + 1):
            sum += self.data[k]
        return sum


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
for left, right in [[0, 2], [2, 5], [0, 5]]:
    print(obj.sumRange(left, right))


# Complexity Analysis
# Time Complexity: O(n) time per query. Each sumRange query takes O(n) time.
# Space Complexity : O(1). Note that data is a reference to nums and is not a copy of it.
