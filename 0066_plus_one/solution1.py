# https://leetcode.com/problems/plus-one/solution/

# Linear Solution

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ''.join(str(x) for x in digits)

        num_int = int(num_str) + 1

        return [int(x) for x in str(num_int)]

# OR

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # using map
        num_str = ''.join(map(str, digits))

        num_int = int(num_str) + 1

        return [int(x) for x in str(num_int)]
    

digits = [1,2,3]
obj = Solution()
print(obj.plusOne(digits))