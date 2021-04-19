class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter=0
        # jewels=set(jewels)
        for i in stones:
            if i in jewels:
                counter+=1
        return counter

jewels = "aA"
stones = "aAAbbbb"
obj = Solution()
print(obj.numJewelsInStones(jewels,stones))
