# Approach 3: DP + Least Significant Bit

# Algorithm:
# We can have a transition function by playing with the least significant bit.
# Let look at the relation between x and x' = x / 2

# x = (1001011101)_2 = (605)_{10}​
# x' = (100101110)_2 = (302)_{10}​

# We can see that x' is different than x by one bit, because x' can be considered as the result of removing the
# least significant bit of x.
# Thus, we have the following transition function of pop count P(x):
# P(x) = P(x/2)+(x.mod2)


from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            # x // 2 is x >> 1 and x % 2 is x & 1
            ans[x] = ans[x >> 1] + (x & 1) 
        return ans 


n = 5
obj = Solution()
print(obj.countBits(n))

# Complexity Analysis:
# Time Complexity: O(N), For each integer x, in the range 1 to n, we need to perform a constant number of 
# operations which does not depend on the number of bits in x.
# Space Complexity: O(1). Since the output array does not count towards the space complexity.
