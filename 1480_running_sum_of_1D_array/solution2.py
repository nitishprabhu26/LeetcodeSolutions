class Solution:
    def runningSum(self, nums: [int]) -> [int]:
        listRunningSum=[]
        sum=0
        for i in range(len(nums)):
            sum +=nums[i]
            listRunningSum.append(sum)
        return listRunningSum


nums = [2, 6, 11, 15]
obj = Solution()
print(obj.runningSum(nums))