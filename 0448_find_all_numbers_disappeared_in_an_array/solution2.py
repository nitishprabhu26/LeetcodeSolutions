# Approach : Using Hashset


from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        nums_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                res.append(i)
        return res


# Approach 1: Using Hash Map

# Intuition:
# The intuition behind using a hash map is pretty clear in this case. We are given that the array would be of size 
# N and it should contain numbers from 1 to N. However, some of the numbers are missing. All we have to do is keep 
# track of which numbers we encounter in the array and then iterate from 1⋯N and check which numbers did not 
# appear in the hash table. Those will be our missing numbers


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Hash table for keeping track of the numbers in the array
        # Note that we can also use a set here since we are not 
        # really concerned with the frequency of numbers.
        hash_table = {}
        
        # Add each of the numbers to the hash table
        for num in nums:
            hash_table[num] = 1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that don't appear in the hash table. 
        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)
                
        return result
        

nums = [4,3,2,7,8,2,3,1]
obj = Solution()
print(obj.findDisappearedNumbers(nums))


# Complexity Analysis:
# Time Complexity: O(N).
# Space Complexity: O(N). No extra space required, other than the space for the output list.
