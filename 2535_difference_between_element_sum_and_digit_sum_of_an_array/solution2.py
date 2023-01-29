# Approach: One liner
# We know that element sum is always greater than digit sum. so we dont need absolute at the end.


from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        # i/p -> nums = [1,15,6,3]

        # convert list of nums to list of strings, and then concatenate them together
        # ''.join(map(str,nums)) -> "11563"

        # convert the string of digits to list of integer digits; and then find sum
        # sum(map(int,list(''.join(map(str,nums))))) -> [1, 1, 5, 6, 3] -> 16

        digitSum = sum(map(int,list(''.join(map(str,nums)))))

        return sum(nums) - digitSum

# OR

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return sum(nums) - sum(int(d) for num in nums for d in str(num))


nums = [1,15,6,3]
obj = Solution()
print(obj.differenceOfSum(nums))


# Complexity Analysis:
# Time complexity : O(N.M). N is the number of elements in input array. M is the number of digits in the largest 
# element of the array.
# Space complexity : O(1).