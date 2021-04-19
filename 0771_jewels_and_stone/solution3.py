# For each stone, check whether it matches any of the jewels. We can check with a linear scan.

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)

jewels = "aA"
stones = "aAAbbbb"
obj = Solution()
print(obj.numJewelsInStones(jewels,stones))

# Complexity Analysis:  
# Time Complexity: O(J.length ∗ S.length).
# Space Complexity: O(1) additional space complexity in Python.