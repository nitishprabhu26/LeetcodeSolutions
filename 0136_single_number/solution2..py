# Approach 1: List operation

class Solution:
    def singleNumber(self, nums):
        list_no_duplicates=[]
        for i in nums:
            if  i not in list_no_duplicates:
                list_no_duplicates.append(i)
            else:
                list_no_duplicates.remove(i)
        return list_no_duplicates.pop()
            
            
nums = [4,1,2,1,2]
obj = Solution()
print(obj.singleNumber(nums))

# Complexity Analysis:
# Time complexity : O(n^2). We iterate through nums, taking O(n) time. We search the whole list to find whether 
# there is duplicate number, taking O(n) time. Because search is in the for loop, so we have to multiply both time 
# complexities which is O(n^2)
# Space complexity : O(n). We need a list of size n to contain elements in nums.