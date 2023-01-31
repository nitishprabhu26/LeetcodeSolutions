# Approach 2: Performance Optimisation : Recursion with Memoization

# - Precompute 38 Tribonacci numbers:
#   - Initiate array of precomputed Tribonacci numbers nums by zeros and initiate the first three numbers.
#   - Return helper(n - 1).
# - Recursive function helper(k):
#   - If k == 0, return 0.
#   - If nums[k] != 0, return nums[k].
#   - Otherwise, nums[k] = helper(k - 1) + helper(k - 2) + helper(k - 3). Return nums[k].
# - Retrieve needed Tribonacci number from the array of precomputed numbers.


class Tri:
    def __init__(self):
        def helper(k):
            if k == 0:
                return 0
            
            if nums[k]:
                return nums[k]

            nums[k] = helper(k - 1) + helper(k - 2) + helper(k - 3) 
            return nums[k]
        
        n = 38
        self.nums = nums = [0] * n
        nums[1] = nums[2] = 1
        helper(n - 1)
                    
class Solution:
    t = Tri()
    def tribonacci(self, n: int) -> int:
        return self.t.nums[n]
        

n = 4
obj = Solution()
print(obj.tribonacci(n))


# Complexity Analysis:
# Time complexity : O(N) to retrieve preliminary computed Tribonacci number, and 38 operations for the preliminary 
# computations.
# Space complexity : constant space to keep an array of 38 Tribonacci numbers.