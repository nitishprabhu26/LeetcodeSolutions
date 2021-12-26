# Similar to Hamming distance (461)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # num % 2 tells if last bit is present or not (gives the last bit) 
            # (checks is number is even or odd)
            count += n % 2
            n >>= 1
        return count
            
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         while n:
#             if n & 1:
#                 count += 1
#             n >>= 1
#         return count

n = 11
obj = Solution()
print(obj.hammingWeight(n))

#  Complexity Analysis:
# Time Complexity: O(1), since the Integer is of fixed size in Python and Java, the algorithm takes a constant 
# time. For an Integer of 32 bit, the algorithm would take at most 32 iterations.
# Space Complexity: O(1), a constant size of memory is used, regardless the input.
