# Approach : Neetcode (Sliding Window)
# https://youtu.be/yYtaV0G3mWQ


import collections
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = collections.defaultdict(int) # fruitType -> countInBasket
        l, total, res = 0, 0, 0
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1
            
            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                total -= 1
                l += 1
                
                if not count[f]:
                    count.pop(f)
            
            res = max(res, total)
        
        return res
    

fruits = [1,2,3,2,2]
obj = Solution()
print(obj.totalFruit(fruits))


# Complexity Analysis:
# Let n be the length of the input array fruits.
# Time Complexity: O(2.n). worst case both left and right pointer iterate throgh the array once.
# Space Complexity: O(1).