# Approach 3: Without Space [Time Limit Exceeded]

# Algorithm:
# Instead of considering all the start and end points and then finding the sum for each subarray corresponding to 
# those points, we can directly find the sum on the go while considering different end points. i.e. We can choose 
# a particular start point and while iterating over the end points, we can add the element corresponding to the 
# end point to the sum formed till now. Whenever the sum equals the required k value, we can update the count 
# value. We do so while iterating over all the end indices possible for every start index. Whenever, we update the 
# start index, we need to reset the sum value to 0.


from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    count += 1
        
        return count

        
nums = [1,2,3]
k = 3
obj = Solution()
print(obj.subarraySum(nums, k))


# Complexity Analysis:
# Time complexity : O(n^2). We need to consider every subarray possible.
# Space complexity : O(1). Constant space is used.