# Approach 0: Sort
# The naive solution would be to sort an array first and then return kth element from the end, something like 
# sorted(nums)[-k] on Python. That would be an algorithm of O(N.logN) time complexity and O(1) space complexity. 
# This time complexity is not really exciting so let's check how to improve it by using some additional space.


from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
        # or
        nums.sort()
        return nums[-k]

# OR

class Solution:
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]


nums = [3,2,3,1,2,4,5,5,6]
k = 4
obj = Solution()
print(obj.findKthLargest(nums, k))


# Complexity Analysis:
# Given n as the length of nums,
# Time complexity: O(n⋅log⁡n).
# Sorting nums requires O(n⋅log⁡n) time.
# Space Complexity: O(n).
# The space complexity of the sorting algorithm depends on the implementation of each programming language:
# - In Java, Arrays.sort() for primitives is implemented using a variant of the Quick Sort algorithm, which has 
#   a space complexity of O(log⁡n).
# - In C++, the sort() function provided by STL uses a hybrid of Quick Sort, Heap Sort, and Insertion Sort, 
#   with a worst-case space complexity of O(logn).
# - In Python, the sort() function is implemented using the Timsort algorithm, which has a worst-case space 
#   complexity of O(n).