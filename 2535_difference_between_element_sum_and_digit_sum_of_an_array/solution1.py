# Approach: Regular approach


from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0
        
        element_sum = sum(nums)
        
        for num in nums:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            digit_sum += total
            
        return abs(element_sum - digit_sum)


nums = [1,15,6,3]
obj = Solution()
print(obj.differenceOfSum(nums))


# Complexity Analysis:
# Time complexity : O(N.M). N is the number of elements in input array. M is the number of digits in the largest 
# element of the array.
# Space complexity : O(1).