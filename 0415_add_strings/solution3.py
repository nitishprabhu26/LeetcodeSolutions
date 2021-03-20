# In Python, the ord() function accepts a string of unit length as an argument and returns the Unicode equivalence of the passed 
# argument. In other words, given string of length 1, the ord() function returns an integer representing the Unicode code point 
# of the character when the argument is a Unicode object, or the value of the byte when the argument is an 8-bit string.

# integer representing the Unicode code
# value = ord("9")
# value1 = ord('0')
# output: 57 48

# https://leetcode.com/problems/add-strings/solution/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        res=[]
        carry=0
        p1,p2=len(num1)-1,len(num2)-1
        
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            p1-=1
            p2-=1
        if carry:
            res.append(carry)
        return ''.join(str(x) for x in res[::-1])

# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
        
#         res=""
#         carry=0
#         p1,p2=len(num1)-1,len(num2)-1
        
#         while p1 >= 0 or p2 >= 0:
#             x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
#             x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
#             value = (x1 + x2 + carry) % 10
#             carry = (x1 + x2 + carry) // 10
#             res=str(value)+res
#             p1-=1
#             p2-=1
#         if carry:
#             res=str(carry)+res
#         return str(res)

num1 = "123"
num2 = "456"

obj = Solution()
print(obj.addStrings(num1, num2))

# Complexity Analysis:
# Time Complexity: O(max(N1,N2))
# Space Complexity: O(max(N1,N2))