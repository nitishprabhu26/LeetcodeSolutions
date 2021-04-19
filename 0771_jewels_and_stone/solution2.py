class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([e for e in list(stones) if e in list(jewels)])

jewels = "aA"
stones = "aAAbbbb"
obj = Solution()
print(obj.numJewelsInStones(jewels,stones))