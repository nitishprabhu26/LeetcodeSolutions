# Approach 3: Mask and Shift
# The idea can be considered as a strategy of divide and conquer, where we divide the original 32-bits into 
# blocks with fewer bits via bit masking, then we reverse each block via bit shifting, and at the end we merge 
# the result of each block to obtain the final result.

# Algorithm
# We can implement the algorithm in the following steps:
# 1). First, we break the original 32-bit into 2 blocks of 16 bits, and switch them.
# 2). We then break the 16-bits block into 2 blocks of 8 bits. Similarly, we switch the position of the 8-bits 
# blocks
# 3). We then continue to break the blocks into smaller blocks, until we reach the level with the block of 1 
# bit.
# 4). At each of the above steps, we merge the intermediate results into a single integer which serves as the 
# input for the next step.

class Solution:
    def reverseBits(self, n: int) -> int:
        n = (n >> 16) | (n << 16)
        # n = ((n & 0xffff0000) >> 16) | ((n & 0x0000ffff) << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


n = 43261596
obj = Solution()
print(obj.reverseBits(n))

# Complexity Analysis:
# Time Complexity: O(1). no loop is used in the algorithm.
# Space Complexity: O(1), Actually, we did not even create any new variable in the function.