# Neetcode - https://youtu.be/keuWJ47xG8g

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        
        # reverse
        a, b = a[::-1], b[::-1]
        
        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0
            
            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2
            
        if carry:
            res = "1" + res
            
        return res
            

a = "11"
b = "1"
obj = Solution()
print(obj.addBinary(a, b))


# Complexity Analysis:
# Time complexity: O(max(N,M)), where N and M are lengths of the input strings a and b.
# Space complexity: O(max(N,M)) to keep the answer.