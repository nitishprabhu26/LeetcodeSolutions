# Neetcode: https://youtu.be/68isPRHgcFQ?si=eZ5GamVXSDEZwxi7


from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans


nums = [1,2,1]
obj = Solution()
print(obj.getConcatenation(nums))
