# Approach 2: Seen-Maximums Set

# Intuition:

# In the previous approach, we deleted the maximum and second maximum so that we could easily find the third 
# maximum. We had to convert the input Array into a Set so that duplicates weren't super complicated to handle.
# Instead of deleting items though, we could instead keep a Set of maximums we've already seen. Then when we are 
# searching for a maximum, we can ignore any values that are already in the seen Set.
# This will also handle duplicates elegantly—if for example we had the input set [12, 12, 4, 2, 12, 1], then the 
# first value we'd put into the seen maximums Set would be 12. Then when we find the second maximum, the algorithm
# knows to ignore all the 12s.


from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
    
        def maximum_ignoring_seen_maximums(nums, seen_maximums):
            maximum = None
            for num in nums:
                if num in seen_maximums:
                    continue
                if maximum == None or num > maximum:
                    maximum = num
            return maximum


        seen_maximums = set()

        for _ in range(3):
            current_maximum = maximum_ignoring_seen_maximums(nums, seen_maximums)
            if current_maximum == None:
                return max(seen_maximums)
            seen_maximums.add(current_maximum)

        return min(seen_maximums)



nums = [3,2,1]
nums = [1,2]
obj = Solution()
print(obj.thirdMax(nums))


# Complexity Analysis:

# Time Complexity : O(n).
# For each of the three times we find the next maximum, we need to perform an O(n) scan. Because there are only, 
# at most, three scans the total time complexity is just O(n).
# The Set operations are all O(1) because there are only at most 3 items in the Set.
# Space Complexity : O(1).
# Because seenMaximums can contain at most 3 items, the space complexity is only O(1).