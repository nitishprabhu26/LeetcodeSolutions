# But we use str to int conversion here - not the right solution

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1)+int(num2))

num1 = "123"
num2 = "456"

obj = Solution()
print(obj.addStrings(num1, num2))