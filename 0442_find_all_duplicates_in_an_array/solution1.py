# Approach 1: Brute Force [Time Limit Exceeded]

# Intuition:
# Check for a second occurrence of every element in the rest of the array.

# Algorithm:
# When we iterate over the elements of the input array, we can simply look for any other occurrence of the current 
# element in the rest of the array.
# Since an element can only occur once or twice, we don't have to worry about getting duplicates of elements that 
# appear twice:
# - Case - I: If an element occurs only once in the array, when you look for it in the rest of the array, you'll 
#   find nothing.
# - Case - II: If an element occurs twice, you'll find the second occurrence of the element in the rest of the 
#   array.When you chance upon the second occurrence in a later iteration, it'd be the same as Case - I (since 
#   there are no more occurrences of this element in the rest of the array).


from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    ans.append(nums[i])
                    
        return ans


nums = [4,3,2,7,8,2,3,1]
obj = Solution()
print(obj.findDuplicates(nums))


# Complexity Analysis:
# Time Complexity: O(n^2). For each element in the array, we search for another occurrence in the rest of the array. 
# Hence, for the i^{{th}} element in the array, we might end up looking through all n - i remaining elements in the 
# worst case. So, we can end up going through about n^2 elements in the worst case.
# Space Complexity: O(1). No extra space required, other than the space for the output list.