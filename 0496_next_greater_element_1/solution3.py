# Approach 2: Better Brute Force

# Algorithm:
# Instead of searching for the occurence of nums1[i] linearly in the nums2 array, we can make use of a hashhash 
# to store the elements of nums2 in the form of (element, index). By doing this, we can find nums1[i]'s index 
# in nums2 array directly and then continue to search for the next larger element in a linear fashion.


from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        for i in range(len(nums2)):
            dict[nums2[i]] = i
            
        res = [-1] * len(nums1)
        
        for i in range(len(nums1)):
            
            for k in range(dict.get(nums1[i]), len(nums2)):
                if nums2[k] > nums1[i]:
                    res[i] = nums2[k]
                    break            
            
        return res
        
        
        
# OR

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        for i in range(len(nums2)):
            dict[nums2[i]] = i
            
        res = [None] * len(nums1)
        
        for i in range(len(nums1)):
            
            for j in range(dict.get(nums1[i]), len(nums2) + 1):
                if j == len(nums2):
                    res[i] = -1
                else:
                    if nums2[j] > nums1[i]:
                        res[i] = nums2[j]
                        break            
            
        return res
        
        
nums1 = [4,1,2]
nums2 = [1,3,4,2]

obj = Solution()
print(obj.nextGreaterElement(nums1, nums2))


# Complexity Analysis:
# Time Complexity: O(m⋅n). The whole nums2 array, of length n, needs to be scanned for all the m elements of 
# nums1 in the worst case. However, in practice, this algorithm will be faster than the previous one, since here 
# we don't need to scan nums2 to find the position of nums1[i] element.
# Space complexity: O(n). A hashmap hashhash of size n is used, where n refers to the length of the nums2 array.
