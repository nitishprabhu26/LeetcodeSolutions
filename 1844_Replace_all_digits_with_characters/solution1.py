class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            if i % 2 == 0:
                ans += s[i]
            else:
                ans += chr(ord(s[i-1])+int(s[i]))
        return ans

s = "a1c1e1"
obj = Solution()
print(obj.replaceDigits(s))
