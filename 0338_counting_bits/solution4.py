# Approach 4: DP + Last Set Bit

# Algorithm:
# Last set bit is the rightmost set bit. Setting that bit to zero with the bit trick, x &= x - 1, leads to the
# following transition function:
# eg:
# x = 5 = 101
# x' = [ x & (x - 1) ] = 100
# its equivalent to adding '+1' to the 1-bit count in x'(since we remove rightmost 1 bit of x to get x')

# P(x) = P( x & (x−1) ) + 1


from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            # x // 2 is x >> 1 and x % 2 is x & 1
            ans[x] = ans[x >> 1] + (x & 1)
        return ans


n = 51
obj = Solution()
print(obj.countBits(n))

# Complexity Analysis:
# Time Complexity: O(N), For each integer x, in the range 1 to n, we need to perform a constant number of
# operations which does not depend on the number of bits in x.
# Space Complexity: O(1). Since the output array does not count towards the space complexity.
