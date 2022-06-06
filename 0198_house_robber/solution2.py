# Approach 1: Recursion with Memoization

# Easiest approach here is to try all possible combinations of house choices and then use the combination that 
# gives the maximum amount of money to the robber. We do this because there is no plausible greedy strategy that 
# we can use to decide if the robber should rob a particular house or not.
# We rely on recursion whenever we have choices involved in solving a problem. Technically, a robber can come back 
# and rob a house that they previously rejected. However, since we are trying all options, we will not go back and 
# rob an unrobbed house since that scenario will be covered in a different recursive path.


# Solution: the 'position' indicates that the robber has yet to scan houses [position,⋯,N] where N represents the 
# total number of houses.
# Naturally, the answer to our problem would be the function call robFrom(0) which means scan all the houses and 
# return the maximum profit. Now let's think about robFrom(i) for a moment. This simply represents a sub-array or 
# a suffix from the main array. We can think about this as a smaller max-profit problem in itself.

# At each step, the robber has two options. If he chooses to rob the current house, he will have to skip the next 
# house on the list by moving two steps forward. If he chooses not to rob the current house, he can simply move on 
# to the next house in the list. mathematically:

# robFrom(i) = max(robFrom(i+1), robFrom(i+2)+nums(i))

# Algorithm:
# 1. We define a function called robFrom() which takes the index of the house that the robber currently has to 
#    examine. 
# 2. At each step of our recursive call, the robber has two options. He can either rob the current house or not.
#     a. If the robber chooses to rob the current house, then he has to skip the next house i.e 
#        robFrom(i + 2, nums). The answer here would be whatever is returned by robFrom(i + 2, nums) in addition 
#        to the amount that the robber will get by robbing the current house i.e. nums[i].
#     b. Otherwise, he can simply move on to the house next door and return whatever profit he will make in the 
#        sub-problem i.e. robFrom(i + 1, nums).
# 3. We need to find, cache, and return the maximum of these two options at each step.
# 4. robFrom(0, nums) will give us the answer to the entire problem.


from typing import List

class Solution:
    
    # def __init__(self):
    #     self.memo = {}  
        
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.robFrom(0, nums)
        
    def robFrom(self, i, nums):
        # No more houses left to examine.
        if i >= len(nums):
            return 0
        
        # Return cached value.
        if i in self.memo:
            return self.memo[i]
        
        # Recursive relation evaluation to get the optimal answer.
        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])
        
        # Cache for future use.
        self.memo[i] = ans
        return ans


nums = [1,2,3,1]
nums = [2,7,9,3,1]
obj = Solution()
print(obj.rob(nums))

# Complexity Analysis:
# Time Complexity: O(N) since we process at most N recursive calls, thanks to caching, and during each of these 
# calls, we make an O(1) computation which is simply making two other recursive calls, finding their maximum, and 
# populating the cache based on that.
# Space Complexity: O(N) which is occupied by the cache and also by the recursion stack.