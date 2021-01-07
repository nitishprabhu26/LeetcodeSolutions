class Solution:
    def runningSum(self, nums: [int]) -> [int]:
        listRunningSum=[]
        for i in range(len(nums)):
            sum = 0
            # for j in range(len(nums)):
            for j in range(0,i+1):
                sum = sum+nums[j]
            listRunningSum.append(sum)
        return listRunningSum

nums = [2, 6, 11, 15]
obj = Solution()
print(obj.runningSum(nums))