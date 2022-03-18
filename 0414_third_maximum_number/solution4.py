# Approach : extra
# using min heap


from typing import List
import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        min_heap = []
        for num in nums:
            if num in min_heap:
                continue
            if len(min_heap) < 3:
                heapq.heappush(min_heap, num)
            elif len(min_heap) == 3:
                heapq.heappushpop(min_heap, num)        
        
        if len(min_heap) == 3:
            return heapq.heappop(min_heap)
        else:
            while min_heap:
                result = heapq.heappop(min_heap)
            return result

nums = [3,2,1]
nums = [1,2]
obj = Solution()
print(obj.thirdMax(nums))


# Complexity Analysis:

# Time Complexity : O(n).
# Space Complexity : O(1).