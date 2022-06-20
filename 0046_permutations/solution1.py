# Approach 1: Backtracking
# Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution 
# candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by 
# making some changes on the previous step, i.e. backtracks and then try again.

# Here is a backtrack function which takes the index of the first integer to consider as an argument 
# backtrack(first).
# 1. If the first integer to consider has index n that means that the current permutation is done.
# 2. Iterate over the integers from index first to index n - 1.
#   -   Place i-th integer first in the permutation, i.e. swap(nums[first], nums[i]).
#   -   Proceed to create all permutations which starts from i-th integer : backtrack(first + 1).
#   -   Now backtrack, i.e. swap(nums[first], nums[i]) back.


from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
                # print(output)
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # print(i, first, nums)
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                # print('reverse')
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output


nums = [1,2,3]
obj = Solution()
print(obj.permute(nums))


# Complexity Analysis:
# https://leetcode.com/problems/permutations/solution/.