# Approach: convert to string; O(N) approach using for loop


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        ans = 0
        
        for i in range(0, len(s), 2):
            ans += int(s[i])
        for i in range(1, len(s), 2):
            ans -= int(s[i])
        
        return ans


# same approach, but in single iteraation

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        ans = 0
        for i in range(len(s)):
            if i % 2 == 0: 
                ans += int(s[i])
            else: 
                ans -= int(s[i])
        return ans


n = 521
obj = Solution()
print(obj.alternateDigitSum(n))


# Complexity Analysis:
# Time complexity : O(N).
# Space complexity : O(1).