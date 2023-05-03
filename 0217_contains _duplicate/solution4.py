# Approach 3 (Hash Table) 


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i,x in enumerate(nums):
            if x in dict:
                return True
            dict[x] = i
        return False


# nums = [1,2,3,1]
nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]
obj = Solution()
print(obj.containsDuplicate(nums))


# Complexity Analysis:
# Time complexity : O(n). We do 'in' and insert(assign) for n times and each operation takes constant time.
# Space complexity : O(n). The space used by a dictionary is linear with the number of elements in it.