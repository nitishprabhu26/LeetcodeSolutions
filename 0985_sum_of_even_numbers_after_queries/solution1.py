# Approach: Brute force apprach


from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        
        for val, idx in queries:
            nums[idx] += val
            total = sum( x for x in nums if x % 2 == 0)
            ans.append(total)
            
        return ans
        

nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
obj = Solution()
print(obj.sumEvenAfterQueries(nums, queries))


# Complexity Analysis:
# Time Complexity: O(Q * N), where N is the length of nums and Q is the number of queries.
# Space complexity : O(Q).