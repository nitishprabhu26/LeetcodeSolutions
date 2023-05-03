# Approach 4 (Hash Set) 


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False


# nums = [1,2,3,1]
nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]
obj = Solution()
print(obj.containsDuplicate(nums))


# Complexity Analysis:
# Time complexity : O(n). We do 'in' and insert(assign) for n times and each operation takes constant time.
# Space complexity : O(n). The space used by a set is linear with the number of elements in it.