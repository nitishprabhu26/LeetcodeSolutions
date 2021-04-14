class Solution:
    def sortedSquares(self, nums: int) -> int:
        return sorted([i*i for i in nums])
        
nums = [-4,-1,0,3,10]
obj = Solution()
print(obj.sortedSquares(nums))

# Complexity Analysis:

# Time Complexity: O(N log N), where N is the length of A.
# Space complexity : O(N) or O(logN)

# The space complexity of the sorting algorithm depends on the implementation of each program language.

# For instance, the list.sort() function in Python is implemented with the Timsort algorithm whose space complexity is O(N).

# In Java, the Arrays.sort() is implemented as a variant of quicksort algorithm whose space complexity is O(logN).