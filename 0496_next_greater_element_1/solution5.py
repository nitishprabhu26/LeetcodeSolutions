# Neetcode: O(n^2) or O(m⋅n) solution 
# https://youtu.be/68a1Dc_qVq4


from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # mapping every single value in nums1 to its index
        nums1Idx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        
        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break            
            
        return res
        
nums1 = [4,1,2]
nums2 = [1,3,4,2]

obj = Solution()
print(obj.nextGreaterElement(nums1, nums2))


# Complexity Analysis:
# Time Complexity: O(n^2) or technically O(m.n), since we are finding next greater element for every value in 
# nums1 and not nums2.
# Space complexity: O(m). A hashmap hashhash of size m is used, where m refers to the length of the nums1 array.
        