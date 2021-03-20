# This is inefficient since we have to calculate the power of 10 every time. High runtime of 360ms
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        int_num1=0
        int_num2=0
        for i,x in enumerate(reversed(num1)):
            int_num1+=int(x)*10**i
        for i,x in enumerate(reversed(num2)):
            int_num2+=int(x)*10**i
        return str(int_num1+int_num2)

# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         int_num1=0
#         int_num2=0
#         for i,x in enumerate(num1):
#             int_num1+=int(x)*10**(len(num1)-1-i)
#         for i,x in enumerate(num2):
#             int_num2+=int(x)*10**(len(num2)-1-i)
#         return str(int_num1+int_num2)

num1 = "123"
num2 = "456"

obj = Solution()
print(obj.addStrings(num1, num2))