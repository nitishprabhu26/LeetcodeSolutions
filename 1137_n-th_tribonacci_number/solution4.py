# Approach 3: Performance Optimisation : Dynamic Programming

# - Precompute 38 Tribonacci numbers:
#   - Initiate array of precomputed Tribonacci numbers nums by zeros and initiate the first three numbers.
#   - Perform the loop for i in a range from 3 to 38. Compute at each step the new Tribonacci number: 
#     nums[i] = helper(i - 1) + helper(i - 2) + helper(i - 3).
# - Retrieve needed Tribonacci number from the array of precomputed numbers.


class Tri:
    def __init__(self):
        n = 38
        self.nums = nums = [0] * n
        nums[1] = nums[2] = 1
        for i in range(3, n):
            nums[i] = nums[i - 1] + nums[i - 2] + nums[i - 3]
                    
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