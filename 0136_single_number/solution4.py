# Approach 3: Math

# Concept: 
# 2 ∗ (a + b + c) − (a + a + b + b + c) = c


class Solution:
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)
            

nums = [4,1,2,1,2]
obj = Solution()
print(obj.singleNumber(nums))


# Complexity Analysis:
# Time complexity : O(n + n) = O(n). sum will call next to iterate through nums. We can see it as 
# sum(list(i, for i in nums)) which means the time complexity is O(n) because of the number of elements(n) in nums.
# Space complexity : O(n + n) = O(n). set needs space for the elements in nums.