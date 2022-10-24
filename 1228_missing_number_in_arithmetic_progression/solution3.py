# Approach 2: Binary Search (video)
# https://leetcode.com/problems/missing-number-in-arithmetic-progression/solution/

# Intuition:
# We know that there is only one missing number in the given progression. At any index i we can figure out if the 
# value at index i is at the correct position by adding difference times i to the first value in the list, and 
# then comparing it with the value at index i. if they match it means the missing value is in an index on the 
# right of i else it's on the left of i or at i.
# This fact can be used to find the index which has the first incorrect number using binary search because if i is 
# the first index with an incorrect number all indices following i would be at incorrect positions (they should be 
# present at 1 position further, since one number is missing) and all numbers before index i will be at correct 
# position. This property is required for binary search to be possible.

# Algorithm:
# 1.Get the value of difference using first and the last element, 
#   difference = last_value - first_value / number_of_values.
# 2.Start with left index lo = 0 and right index hi = arr.size() - 1.
# 3.Pick a mid point index mid = (lo + hi) / 2.
# 4.If arr[mid] == first_element + mid * difference. Binary search on the right of mid else binary search on left 
#   side of mid including mid itself.
# 5.End when there is a single index left as this would be the first index with incorrect value.
# 6.Return the value supposed to be at this index which would be first_element + difference * index.


from typing import List

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Get the difference `difference`.
        difference = (arr[-1] - arr[0]) // n
        lo = 0
        hi = n - 1
        
        # Basic binary search template
        while lo < hi:
            mid = (lo + hi) // 2
            
            # All numbers upto `mid` have no missing number, so search on the right side
            if arr[mid] == arr[0] + mid * difference:
                lo = mid + 1
            # A number is missing before `mid` inclusive of `mid` itself.
            else:
                hi = mid
                
        # Index `lo` will be the position with the first incorrect number.
        # Return the value that was supposed to be at this index
        return arr[0] + difference * lo


arr = [5,7,11,13]
obj = Solution()
print(obj.missingNumber(arr))


# Complexity Analysis:
# Time complexity : O(logn). 
# Where n is the length of array and since we cut the search space in half at every iteration.
# Space complexity : O(1). Algorithm requires constant space to execute.