# Approach1: Using sort function (Not advisable.)

class Solution:
    def findMedianSortedArrays(self, nums1: int, nums2: int) -> float:
        final_array = nums1 + nums2
        final_array.sort()
        med = 0
        length = len(final_array)
        if length % 2 == 0:
            med = (final_array[length//2] + final_array[length//2-1])/2
        else:
            med = final_array[length//2]
        return med


nums1 = [1, 2]
nums2 = [3, 4]
obj = Solution()
print(obj.findMedianSortedArrays(nums1, nums2))


# Complexity Analysis:
# Time complexity : O((m+n).log(m+n)). Sort is used on the combined array.
# Space complexity : O(m+n). extra space is used to store the final_array, and later sorting is applied.