class Solution:
    def singleNumber(self, nums: [int]) -> int:
        dict={}
        for i in nums:
            dict[i]=dict.get(i,0)+1
        for i,j in dict.items():
            if j ==1:
                return i
            
nums = [4,1,2,1,2]
obj = Solution()
print(obj.singleNumber(nums))

# Complexity Analysis:
# Time Complexity: O(N), where N is the length of nums.
# Space Complexity: O(N)