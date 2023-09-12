# Simple solution using the division operation : O(n)


from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)

        if nums_len == 2:
            return [nums[1], nums[0]]
        
        product = 1
        zeroCount = 0
        zeroIndex = 0

        for i, num in enumerate(nums):
            if num == 0:
                zeroCount += 1
                if zeroCount > 1:
                    product = 0
                    break
                zeroIndex = i
            else:
                product *= num
        
        result = [0] * nums_len

        # If there are one or more zeros in the array
        if zeroCount > 0:
            if product == 0:
                return result
            result[zeroIndex] = product
        else:
            for i, num in enumerate(nums):
                result[i] = product//num
        
        return result


nums = [1,2,3,4]
obj = Solution()
print(obj.productExceptSelf(nums))


# Complexity analysis:
# Time complexity : O(N) where N represents the number of elements in the input array.
# Space complexity : O(1) ignoring the array to store result.
