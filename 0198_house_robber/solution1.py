# Neetcode - Best solution out of all
# https://youtu.be/73r3KWiEvyk

class Solution:
    def rob(self, nums: [int]) -> int:
        rob1, rob2 = 0,0
        
        # [rob1, rob2, n, n+1 ....]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


nums = [1,2,3,1]
# nums = [2,7,9,3,1]
obj = Solution()
print(obj.rob(nums))

# Complexity analysis:
# Time Complexity: O(N)
# Space Complexity: O(1) since simply using three variables for our calculations.