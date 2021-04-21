# Ref: https://www.youtube.com/watch?v=YyHmAEQ6y6Q

class Solution(object):
    def deleteAndEarn(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            nums.sort()
            a = nums[0]
            b = nums[1]
            if a+1 == b:
                return b
            else:
                return a+b

        m = max(nums)
        dp = [0]*(m+1)
        for n in nums:
            dp[n] += n
        len_dp=len(dp)
        dp[len_dp-2]= max(dp[len_dp-2],dp[len_dp-1])
        for i in range(len_dp-3,-1,-1):
            dp[i]=max(dp[i+1], dp[i]+dp[i+2])
        return dp[0]
            
nums = [2,2,3,3,3,3,4,6]
obj = Solution()
print(obj.deleteAndEarn(nums))