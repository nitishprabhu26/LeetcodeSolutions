# Approach 2: Hash Table

# Algorithm:
# We use hash table to avoid the O(n) time required for searching the elements.
# - Iterate through all elements in nums and set up key/value pair.
# - Return the element which appeared only once.


from collections import defaultdict

class Solution:
    def singleNumber(self, nums):
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i
            
            
nums = [4,1,2,1,2]
obj = Solution()
print(obj.singleNumber(nums))


# Complexity Analysis:
# Time complexity : O(n.1) = O(n). Time complexity of for loop is O(n). Time complexity of hash table (dictionary 
# in python) operation pop is O(1).
# Space complexity : O(n). The space required by hash_table is equal to the number of elements in nums.
