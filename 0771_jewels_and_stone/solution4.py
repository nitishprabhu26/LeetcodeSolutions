# For each stone, check whether it matches any of the jewels. We can check efficiently with a Hash Set.

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        Jset = set(jewels)
        return sum(s in Jset for s in stones)

jewels = "aA"
stones = "aAAbbbb"
obj = Solution()
print(obj.numJewelsInStones(jewels,stones))

# Complexity Analysis:
# Time Complexity: O(J.length+S.length). The O(J.length) part comes from creating J. TheO(S.length) part comes from searching S.
# Space Complexity: O(J.length).