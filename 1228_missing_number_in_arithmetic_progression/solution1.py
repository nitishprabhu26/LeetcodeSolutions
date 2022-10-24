# Approach: Finding smallest difference with Linear search


from typing import List

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        smallest_diff = max(arr)
        
        is_ascending = True
        if arr[-1] - arr[0] > 0:
            is_ascending = True
        else:
            is_ascending = False
            
        expected = arr[0]
        if is_ascending:
            for i in range(len(arr) - 1):
                smallest_diff = min(smallest_diff, arr[i + 1] - arr[i])
            for val in arr:
                if val != expected:
                    break
                expected += smallest_diff
        else:
            for i in range(len(arr) - 1):
                smallest_diff = min(smallest_diff, abs(arr[i] - arr[i + 1]))
            for val in arr:
                if val != expected:
                    break
                expected -= smallest_diff
                
        return expected


arr = [5,7,11,13]
obj = Solution()
print(obj.missingNumber(arr))


# Complexity Analysis:
# Time complexity : O(n). Where n is the length of array, since in the worst case we iterate over the entire array.
# Space complexity : O(1). Algorithm requires constant space to execute.