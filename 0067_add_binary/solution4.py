# Approach 2: Bit Manipulation

# Algorithm:
# - Convert a and b into integers x and y, x will be used to keep an answer, and y for the carry.
# - While carry is nonzero: y != 0:
#   - Current answer without carry is XOR of x and y: answer = x^y.
#   - Current carry is left-shifted AND of x and y: carry = (x & y) << 1.
#   - Job is done, prepare the next loop: x = answer, y = carry.
# - Return x in the binary form.


# class Solution:
#     def addBinary(self, a, b) -> str:
#         x, y = int(a, 2), int(b, 2)
#         while y:
#             answer = x ^ y
#             carry = (x & y) << 1
#             x, y = answer, carry
#         return bin(x)[2:]
    

class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]
        

a = "11"
b = "1"
obj = Solution()
print(obj.addBinary(a, b))


# Complexity Analysis:
# Time complexity: O(max(N,M)), where N and M are lengths of the input strings a and b.
# Space complexity: O(max(N,M)) to keep the answer.