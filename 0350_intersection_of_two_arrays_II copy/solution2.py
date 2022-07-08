# Approach 2: Sort:

# You can recommend this method when the input is sorted, or when the output needs to be sorted. Here, we sort 
# both arrays (assuming they are not sorted) and use two pointers to find common numbers in a single scan.

# Algorithm:
# 1.Sort nums1 and nums2.
# 2.Initialize i, j and k with zero.
# 3.Move indices i along nums1, and j through nums2:
#   - Increment i if nums1[i] is smaller.
#   - Increment j if nums2[j] is smaller.
#   - If numbers are the same, copy the number into nums1[k], and increment i, j and k.
# 5.Return first k elements of nums1.


from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
            
        i, j, k = 0, 0, 0
        # Move indices i along nums1, and j through nums2:
        while i < len(nums1) and j < len(nums2):
            # Increment i if nums1[i] is smaller.
            if nums1[i] < nums2[j]:
                i += 1
            # Increment j if nums2[j] is smaller.
            elif nums1[i] > nums2[j]:
                j += 1
            # If numbers are the same, copy the number into nums1[k], and increment i, j and k.
            else:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
                
        # Return first k elements of nums1  
        return nums1[:k]


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
obj = Solution()
print(obj.intersect(nums1, nums2))


# Complexity Analysis:
# Time Complexity: O(n.log n + m.log m), where n and m are the lengths of the arrays. We sort two arrays 
# independently, and then do a linear scan.
# Space Complexity: from O(log n + log m) to O(n + m), depending on the implementation of the sorting algorithm. 
# For the complexity analysis purposes, we ignore the memory required by inputs and outputs.