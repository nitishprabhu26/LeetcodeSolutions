# check leetcode solution explaination:

import collections
class Solution(object):
    def deleteAndEarn(self, nums):
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0
        for k in sorted(count):
            print("k: ",k)
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
                print("notAdj",avoid,using)
            else:
                avoid, using = max(avoid, using), k * count[k] + avoid
                print("adj",avoid,using)
            prev = k
        return max(avoid, using)
            
nums = [2,2,3,3,3,3,4,6]
obj = Solution()
print(obj.deleteAndEarn(nums))

# Complexity Analysis:
# Time Complexity (Python): O(NlogN), where N is the length of nums. We make a single pass through the sorted keys of N,
# and the complexity is dominated by the sorting step.
# Space Complexity (Python): O(N), the size of our count.