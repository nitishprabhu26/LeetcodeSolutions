class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
            
            
n = 0b11111111111111111111111111111101
obj = Solution()
print(obj.hammingWeight(n))

# Complexity Analysis:
# Time Complexity: O(1)
# Space Complexity: O(1)