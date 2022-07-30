# Approach 1: Binary search

# Intuition:
# Let's review binary search a bit. Given a sorted array, binary search works by looking at the middle element of 
# the given array, and based on the value of the middle element, it decides to discard one half of the array. At 
# each step, we reduce the length of the array to search by half and that is what leads to the logarithmic time 
# complexity of the algorithm. Usually, we employ the binary search algorithm to determine if an element is in a 
# sorted array. Here, we can tweak the binary search algorithm to find the first and the last position of a given 
# element.

# Algorithm:
# 1. Define a function called findBound which takes three arguments: the array, the target to search for, and a 
#    boolean value isFirst which indicates if we are trying to find the first or the last occurrence of target.
# 2. We use 2 variables to keep track of the subarray that we are scanning. Let's call them begin and end. 
#    Initially, begin is set to 0 and end is set to the last index of the array.
# 3. We iterate until begin is greater than or equal to end.
# 4. At each step, we calculate the middle element mid = (begin + end) / 2. We use the value of the middle element 
#    to decide which half of the array we need to search.
#    a. nums[mid] == target:
#       -   isFirst is true:
#           ~   This implies that we are trying to find the first occurrence of the element. If mid == begin or 
#               nums[mid - 1] != target, then we return mid as the first occurrence of the target. Otherwise, we 
#               update end = mid - 1
#       -   isFirst is false:
#           ~   This implies we are trying to find the last occurrence of the element. If mid == end or 
#               nums[mid + 1] != target, then we return mid as the last occurrence of the target. Otherwise, 
#               we update begin = mid + 1
#    b. nums[mid] > target:
#       -   We update end = mid - 1 since we must discard the right side of the array as the middle element 
#           is greater than target.
#    c. nums[mid] < target:
#       -   We update begin = mid + 1 since we must discard the left side of the array as the middle element 
#           is less than target.
# 5. We return a value of -1 at the end of our function which indicates that target was not found in the array.
# 6. In the main searchRange function, we first call findBound with isFirst set to true. If this value is -1, we 
#    can simply return [-1, -1]. Otherwise, we call findBound with isFirst set to false to get the last occurrence 
#    and then return the result.


from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)
        
        return [lower_bound, upper_bound]
    
    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:  
        N = len(nums)
        begin, end = 0, N - 1
        
        while begin <= end:
            mid = int((begin + end) / 2)    
            
            if nums[mid] == target:
                
                if isFirst:
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    # Search on the left side for the bound.
                    end = mid - 1
                else:
                    
                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    
                    # Search on the right side for the bound.
                    begin = mid + 1
            
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        
        return -1


nums = [5,7,7,8,8,10]
target = 8
obj = Solution()
print(obj.searchRange(nums, target))


# Complexity Analysis:
# Time complexity : O(logN) considering there are N elements in the array. This is because binary search takes 
# logarithmic time to scan an array of N elements. Why? Because at each step we discard half of the array we are 
# scanning and hence, we're done after a logarithmic number of steps. We simply perform binary search twice in 
# this case. 
# Space complexity : O(1) since we only use space for a few variables and our result array, all of which require 
# constant space.

