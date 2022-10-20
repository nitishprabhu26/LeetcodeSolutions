# https://leetcode.com/problems/complement-of-base-10-integer/solution/

# Approach 4: highestOneBit OpenJDK algorithm from Hacker's Delight
# The idea is to create the same 1-bits bitmask by propagating the highest 1-bit into the lower ones.(animation)


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        # bitmask has the same length as N and contains only ones 1...1
        bitmask = N
        bitmask |= (bitmask >> 1)
        bitmask |= (bitmask >> 2)
        bitmask |= (bitmask >> 4)
        bitmask |= (bitmask >> 8)
        bitmask |= (bitmask >> 16)
        # flip all bits
        return bitmask ^ N
        
        
n = 5
obj = Solution()
print(obj.bitwiseComplement(n))


# Complexity
# Time Complexity: O(1).
# Space Complexity: O(1).