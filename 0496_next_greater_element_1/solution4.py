# Approach 3: Using Stack
# https://leetcode.com/problems/next-greater-element-i/solution/ (animation)

# Algorithm:
# In this approach, we make use of pre-processing first so as to make the results easily available later on. We 
# make use of a stack (stack) and a hashmap (map). map is used to store the result for every posssible number in 
# nums2 in the form of (element,next_greater_element). Now, we will look at how to make entries in map.

# We iterate over the nums2 array from the left to right. We push every element nums2[i] on the stack if it is 
# less than the previous element on the top of the stack (stack[top]). No entry is made in map for such nums2[i]'s 
# right now. This happens because the nums2[i]'s encountered so far are coming in a descending order.

# If we encounter an element nums2[i] such that nums2[i] > stack[top], we keep on popping all the elements from 
# stack[top] until we encounter stack[k] such that stack[k] ≥ nums2[i]. For every element popped out of the stack
# stack[j], we put the popped element along with its next greater number (result) into the hashmap mapmap, in the 
# form (stack[j], nums2[i]). Now, the next greater element for all elements stack[j], such that k < j ≤ top is 
# nums2[i] (since this larger element caused all the stack[j]'s to be popped out). We stop popping the elements 
# at stack[k] because this nums2[i] can't act as the next greater element for the next elements on the stack.

# Thus, an element is popped out of the stack whenever a next greater element is found for it. Therefore, the 
# elements remaining in the stack are the ones for which no next greater element exists in the nums2 array. Thus, 
# at the end of the iteration over nums2, we pop the remaining elements from the stack and put their entries in 
# hash with a -1 as their corresponding results.

# Then, we can simply iterate over the nums1 array to find the corresponding results from map directly.

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        # element : next_greater_element
        hashMap = {}
        
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[i] > stack[-1]:
                hashMap[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        while len(stack) > 0:
            hashMap[stack.pop()] = -1
        
        res = [None] * len(nums1)
        
        for i in range(len(nums1)):
            res[i] = hashMap.get(nums1[i])
            
        return res
        
        
nums1 = [4,1,2]
nums2 = [1,3,4,2]

obj = Solution()
print(obj.nextGreaterElement(nums1, nums2))


# Complexity Analysis:
# Let n and m represent the length of the nums2 and nums1 array respectively.
# Time complexity: O(n). The entire nums2 array (of size n) is scanned only once. Each of the stack's n elements 
# are pushed and popped exactly once. The nums1 array is also scanned only once. All together this requires 
# O(n + n + m) time. Since nums1 must be a subset of nums2, we know m must be less than or equal to n. Therefore, 
# the time complexity can be simplified to O(n).
# Space complexity: O(n). map will store n key-value pairs while stack will contain at most n elements at any 
# given time.
