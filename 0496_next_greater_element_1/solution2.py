# Approach 1: Brute Force

# Algorithm:
# In this method, we pick up every element of the nums1 array (say nums1[i]) and then search for its own 
# occurence in the nums2 array (which is indicated by setting found to True). After this, we look linearly for 
# a number in nums2 which is greater than nums1[i], which is also added to the res array to be returned. If no 
# such element is found, we put a -1 at the corresponding location.


from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        j = 0
        
        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if found and nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
                if nums1[i] == nums2[j]:
                    found = True
        return res
        
# OR

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [None] * len(nums1)
        
        for i in range(len(nums1)):
            found = False
            j = 0
            
            for j in range(len(nums2) + 1):
                if j == len(nums2):
                    res[i] = -1
                else:
                    if found and nums2[j] > nums1[i]:
                        res[i] = nums2[j]
                        break
                    if nums1[i] == nums2[j]:
                        found = True
            
        return res
        
        
        
        
nums1 = [4,1,2]
nums2 = [1,3,4,2]

obj = Solution()
print(obj.nextGreaterElement(nums1, nums2))


# Complexity Analysis:
# Time Complexity: O(m⋅n). The complete nums2 array (of size n) needs to be scanned for all the m elements of 
# nums1 in the worst case. the worst case.
# Space complexity: O(1). We do not count the space required to create the output array. Other than that, only 
# constant space is used.
