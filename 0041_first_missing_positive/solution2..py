# Approach 1: Index as a hash key.
# https://leetcode.com/problems/first-missing-positive/solution/

# Algorithm:
# - Check if 1 is present in the array. If not, you're done and 1 is the answer.
# - Replace negative numbers, zeros, and numbers larger than n by 1s.
# - Walk along the array. Change the sign of a-th element if you meet number a. Be careful with duplicates : do 
#   sign change only once. Use index 0 to save an information about presence of number n since index n is not 
#   available.
# - Walk again along the array. Return the index of the first positive element.
# - If nums[0] > 0 return n.
# - If on the previous step you didn't find the positive element in nums, that means that the answer is n + 1.


from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Base case.
        if 1 not in nums:
            return 1
        
        # Replace negative numbers, zeros, and numbers larger than n by 1s.
        # (since the first missing positive is for sure smaller or equal to n + 1.)
        # After this convertion nums will contain only positive numbers (in a range from 1 to n)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1` is present in the array. 
        # If nums[2] is positive - number 2 is missing.
        for i in range(n): 
            # to handle duplicate case
            a = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
            
        # Now the index of the first positive number is equal to first missing positive.
        for i in range(1, n):
            if nums[i] > 0:
                return i
        # index 0 is used to save information about presence of number n 
        # since index n is not available.
        if nums[0] > 0:
            return n
            
        return n + 1
            
nums = [1,2,0]
nums = [3,4,-1,1]
nums = [7,8,9,11,12]
obj = Solution()
print(obj.firstMissingPositive(nums))


# Complexity Analysis:
# Time Complexity: O(N), since all we do here is four walks along the array of length N.
# Space Complexity: O(1) since this is a constant space solution.