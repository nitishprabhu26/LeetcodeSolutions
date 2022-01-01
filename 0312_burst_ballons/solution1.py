# Neetcode
# https://youtu.be/VFskby7lUbw
# Try to pop the lowest number first so that the sum value increases.

# Special Case:
# Now our time complexity is O(N^3)
# Are there any other rooms to optimize? Note that if the array has some special properties, we may be able to 
# calculate the result very fast.

# For example, if all the numbers are the same, the answer is straight forward.
# Let N be the length of nums, and a be the element in nums. The coins we gain, no matter which one is burst, 
# are always (a * a * a), since all balloons are the same, except the last two balloons. For the last two balloons, 
# one yields (a * a * 1), and the other yields (1 * a * 1).
# Therefore, we have (N-2) * (a * a * a), one (a * a * 1), and one (1 * a * 1). Adding together, we have 
# (N - 2) * (a * a * a) + (a * a) + a.
# We can improve the performance sightly by handling those special cases one by one. However, please notice 
# that this optimization does not improve the time complexity and can not speed up too much if the input is 
# highly randomized.


from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        # It throws an TLE which can be fixed by handling the special case which all elements in the list are
        #  the same number.    
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]
        
        nums = [1] + nums + [1]
        dp = {}
        
        def dfs(l, r):
            
            if l > r:
                return 0
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            
            return dp[(l, r)]
            
        # we dont consider the 1's we added to the input
        return dfs(1, len(nums) - 2)

nums = [3,1,5,8]
obj = Solution()
print(obj.maxCoins(nums))

# Complexity Analysis:
# Time Complexity: O(n^3). 
# Space Complexity : O(n^2).

