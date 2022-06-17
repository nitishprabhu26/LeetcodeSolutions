# Approach 3: Store Seen Elements in a Set / Map

# Intuition:
# In Approach 1 we used two loops (one nested within the other) to look for two occurrences of an element. In 
# almost all similar situations, you can usually substitute one of the loops with a set / map. Often, it's a 
# worthy trade-off: for a bit of extra memory, you can reduce the order of your runtime complexity.

# Algorithm:
# We store all elements that we've seen till now in a map / set. When we visit an element, we query the map / set 
# to figure out if we've seen this element before.


from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        seen = set()
        
        for num in nums:
            if num in seen:
                ans.append(num)
            else:
                seen.add(num)
                    
        return ans


nums = [4,3,2,7,8,2,3,1]
obj = Solution()
print(obj.findDuplicates(nums))


# Complexity Analysis:
# Time Complexity: O(n) average case. O(n^2) worst case.
# It takes a linear amount of time to iterate through the array.
# Lookups in a hashset are constant time on average, however those can degrade to linear time in the worst case. 
# Note that an alternative is to use tree-based sets, which give logarithmic time lookups always.
# Space Complexity: Upto O(n) extra space required for the set.
