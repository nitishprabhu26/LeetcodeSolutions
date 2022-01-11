# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         sum = int(a, 2) + int(b, 2)
#         return bin(sum).replace("0b", "")

# OR

# https://thepythonguru.com/python-string-formatting/
# O(N+M) time complexity
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return bin(int(a, 2) + int(b, 2))[2:]

a = "11"
b = "1"
obj = Solution()
print(obj.addBinary(a, b))
