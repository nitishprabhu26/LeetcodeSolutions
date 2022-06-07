# Approach 1: Merge and sort

# Intuition:
# A naive approach would be to simply write the values from nums2 into the end of nums1, and then sort nums1.


from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Write the elements of num2 into the end of nums1.
        for i in range(n):
            nums1[i + m] = nums2[i]
        
        # Sort nums1 list in-place.
        nums1.sort()
        print(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
obj = Solution()
obj.merge(nums1, m, nums2, n)


# Complexity Analysis:
# Time complexity: O((n + m).log(n + m)).
# The cost of sorting a list of length x using a built-in sorting algorithm is O(x.logx). Because in this case 
# we're sorting a list of length m + n, we get a total time complexity of O((n + m).log(n + m)).
# Space complexity: O(n), but it can vary.
# Most programming languages have a built-in sorting algorithm that uses O(n) space.