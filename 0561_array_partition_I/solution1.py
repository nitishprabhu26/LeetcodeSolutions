# Approach 1: Sorting

# Suppose x is the smallest possible element in the given list. This means that the contribution to the answer for 
# any pair that includes x must be x, irrespective of the paired element. The other element will essentially be 
# wasted. Hence to minimize our losses, we would like to pair x with the smallest element other than x.

# Intuition:
# We will sort the given list using the built-in sorting function. In the sorted list we will pair the first two 
# elements then the next two elements and so on. Therefore, the first element (at index 0) will be added to the 
# answer maxSum as it is the minimum of the first two elements. Similarly, the third element in the list (at index 
# 2) will be added, and so on. Hence, we will only sum the elements located at the even indices.

# Algorithm:
# 1. Sort the list nums.
# 2. Initialize the answer variable maxSum as 0.
# 3. Iterate over the list nums and add the elements at even indices to maxSum.
# 4. Return maxSum.


from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the list in ascending order
        nums.sort()
        # Initialize sum to zero
        max_sum = 0
        for i in range(0, len(nums), 2):
            # Add every element at even positions (0-indexed)
            max_sum += nums[i]
            
        return max_sum
            

nums = [6,2,6,5,1,2]
obj = Solution()
print(obj.arrayPairSum(nums))


# Complexity Analysis:
# Here, N is the number of pairs that will be produced (i.e., the size of list nums is 2⋅N).
# Time complexity: O(N.log N)
# Sorting the list nums of size 2⋅N will take O(2⋅N.log(2⋅N)) time which is equivalent to O(N.logN), and iterating 
# over the list will take an additional O(N) time. Hence, the time complexity is O(N.log N).
# Space complexity: O(N)
# The only variable we need is maxSum, which takes O(1) space. However, some space will be used for sorting the 
# list nums. The space complexity of the sorting algorithm depends on the implementation of each programming 
# language. For instance, in Java, the Arrays.sort() for primitives is implemented as a variant of the QuickSort 
# algorithm whose space complexity is O(logN). In C++, sort() function provided by STL is a hybrid of QuickSort, 
# Heap Sort, and Insertion Sort and has a worst-case space complexity of O(logN). Python, on the other hand, uses 
# Timsort, which has a space complexity of O(N). Thus, the use of the built-in sort() function could add up to 
# O(N) to the space complexity.